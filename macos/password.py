
from Security import (SecItemCopyMatching, kSecClass, kSecAttrAccount, kSecAttrService, kSecReturnData,
                      kSecClassGenericPassword, kSecPropertyTypeSuccess)


class PasswordManager:
    def get_wifi_password(self, ssid):
        # Define the query for the Keychain
        query = {
            kSecClass: kSecClassGenericPassword,
            kSecReturnData: True,
            kSecAttrAccount: ssid
        }
    
        status, data = SecItemCopyMatching(query, None)
        if status == 0:
            psw = data.bytes().tobytes()
            return psw.decode()
        else:
            return None
    
