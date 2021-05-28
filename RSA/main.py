from keys import *
from hash import *


if __name__ == "__main__":
    message = input("Enter the message you want to encrypt: ")

    hash_pair = HashPair(16)
    hash_message = Hash(message, hash_pair.p, hash_pair.q)

    rsa = RSA(16)
    closed_pair = ClosedPair(rsa.d, rsa.r)
    encrypted_message = mod_exp(hash_message.h, closed_pair.d, closed_pair.r)

    print(f"\nHash-function '{message}' = {hash_message.h}")
    print(f"Closed pair: r = {closed_pair.r}, d = {closed_pair.d}")
    print(f"\nEncrypted hash-function = {encrypted_message}")

    del message
    del closed_pair
    del hash_message

    sent_message = input("\nWhat message should be sent to the recipient: ")

    hash_message = Hash(sent_message, hash_pair.p, hash_pair.q)

    open_pair = OpenPair(rsa.e, rsa.r)
    decrypted_message = mod_exp(encrypted_message, open_pair.e, open_pair.r)

    print("\n" * 99)
    print(f"You received: ({sent_message}, {encrypted_message})")
    print(f"Open pair: r = {open_pair.r}, d = {open_pair.e}")

    del rsa
    del hash_pair
    del open_pair

    print(f"\nHash-function '{sent_message}' = {hash_message.h}")
    print(f"Decrypted message = {decrypted_message}\n")

    if hash_message.h != decrypted_message:
        print(f"Since the two calculated values {hash_message.h} and {decrypted_message} are not equal,"
              f" the signature is INVALIDATED")
    else:
        print(f"Since the two calculated values {hash_message.h} and {decrypted_message} are equal,"
              f" the signature is VALID")
