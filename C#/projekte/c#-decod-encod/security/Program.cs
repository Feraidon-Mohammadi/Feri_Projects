using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;


namespace System.Security.Cryptography
{
   class program
    {
        static void Main(string[] args)
        {
            // Your code goes here
            string plainText = "this text wird encrypted"; // The text to encrypt
            byte[] key = new byte[] { 0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F };
            byte[] iv = new byte[] { 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F };

            byte[] encrypted = AesEncryption.Encrypt(Encoding.UTF8.GetBytes(plainText), key, iv);
            Console.WriteLine(Convert.ToBase64String(encrypted));

         
        }

        public class AesEncryption
        {
            public static byte[] Encrypt(byte[] plainText, byte[] key, byte[] iv)
            {
                Aes aes = Aes.Create();
                aes.Key = key;
                aes.IV = iv;
                aes.Mode = CipherMode.CBC;
                aes.Padding = PaddingMode.PKCS7;
                ICryptoTransform encryptor = aes.CreateEncryptor();
                using MemoryStream msEncrypt = new MemoryStream();
                using CryptoStream csEncrypt = new CryptoStream(msEncrypt, encryptor, CryptoStreamMode.Write);
                csEncrypt.Write(plainText, 0, plainText.Length);
                csEncrypt.FlushFinalBlock();
                return msEncrypt.ToArray();
            }
        }
   }


    



/* Decrypte the encrypted codes von oben */
/*########################################## decrypt ################################################*/




        class Program
        {
            static void Main(string[] args)
            {
                string encryptedText = "this text should be decrypted"; // The text to decrypt
                byte[] key = new byte[] { 0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F };
                byte[] iv = new byte[] { 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F };
                byte[] decrypted = AesEncryption.Decrypt(Convert.FromBase64String(encryptedText), key, iv);
                string plainText = Encoding.UTF8.GetString(decrypted);
                Console.WriteLine(plainText);
            }

            public class AesEncryption
            {
                public static byte[] Decrypt(byte[] encryptedText, byte[] key, byte[] iv)
                {
                    Aes aes = Aes.Create();
                    aes.Key = key;
                    aes.IV = iv;
                    aes.Mode = CipherMode.CBC;
                    aes.Padding = PaddingMode.PKCS7;
                    ICryptoTransform decryptor = aes.CreateDecryptor();
                    using MemoryStream msDecrypt = new MemoryStream(encryptedText);
                    using CryptoStream csDecrypt = new CryptoStream(msDecrypt, decryptor, CryptoStreamMode.Read);
                    byte[] plainTextBytes = new byte[encryptedText.Length];
                    int decryptedByteCount = csDecrypt.Read(plainTextBytes, 0, plainTextBytes.Length);
                    byte[] decryptedBytes = new byte[decryptedByteCount];
                    Array.Copy(plainTextBytes, decryptedBytes, decryptedByteCount);
                    return decryptedBytes;
                }
            }



        }
    




}
