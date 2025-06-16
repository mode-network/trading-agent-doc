import sha3
from eth_abi import (
    encode as encode_abi_parameters,
)  # Use 'encode' from eth_abi


# Helper: Computes keccak256 hash and returns 32-byte digest.
def keccak256(data: bytes) -> bytes:
    k = sha3.keccak_256()
    k.update(data)
    return k.digest()


# Helper: Mimics Solidity's encodePacked for a limited set of types.
def encode_packed(types: list[str], values: list) -> bytes:
    result = b""
    for t, v in zip(types, values):
        if t == "string":
            result += v.encode("utf-8")
        else:
            raise NotImplementedError(
                f"Packed encoding for type '{t}' is not implemented."
            )
    return result


def account_id_from_address(address: str) -> str:
    # First, compute the inner hash:
    # keccak256(encodePacked(['string'], ['mode']))
    inner_packed = encode_packed(["string"], ["mode"])
    inner_hash = keccak256(inner_packed)

    # Then ABI-encode the parameters: (address, bytes32).
    abi_encoded = encode_abi_parameters(
        ["address", "bytes32"], [address, inner_hash]
    )

    # Finally, return keccak256(abi_encoded) as a hex string.
    final_hash = keccak256(abi_encoded)
    return "0x" + final_hash.hex()
