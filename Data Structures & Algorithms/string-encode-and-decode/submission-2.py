class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(s)
            parts.append("-")
        encoded_string = "".join(parts)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        parts = s.split("-")
        parts.pop()
        decoded_strs = []
        for part in parts:
            decoded_strs.append(part)
        return decoded_strs
        

