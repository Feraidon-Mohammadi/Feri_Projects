using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;




/*
 
 Um Daten in C# mit AES oder RSA zu verschlüsseln und zu entschlüsseln, gibt es verschiedene Bibliotheken und Methoden. Hier sind einige Schritte,

um dies zu erreichen: Fügen Sie das System.Security.Cryptography-Namespace zu Ihrer Anwendung hinzu.

Erstellen Sie eine Instanz der entsprechenden Kryptografieklasse, entweder Aes für AES oder RSACryptoServiceProvider für RSA.

Konfigurieren Sie die Parameter für den Verschlüsselungs- oder Entschlüsselungsvorgang, wie z.B. Schlüssellänge, Verschlüsselungsmethode, Padding-Modus, etc.


Verwenden Sie die Encrypt-Methode des Aes-Objekts oder die Encrypt-Methode des RSACryptoServiceProvider-Objekts, um die Daten zu verschlüsseln.

Verwenden Sie die Decrypt-Methode des Aes-Objekts oder die Decrypt-Methode des RSACryptoServiceProvider-Objekts, um die verschlüsselten Daten zu entschlüsseln.

 */



// sercur namespace 
namespace System.Security.Cryptography
{
    /// <summary>
    /// 
    /// Die Klasse AesEncryption enthält eine statische Methode Encrypt(), die einen Byte-Array mit dem Klartext,
    /// <br />
    /// einem Schlüssel und einem Initialisierungsvektor (IV) als Parameter annimmt und einen Byte-Array mit dem verschlüsselten Text zurückgibt.
    /// <br />
    /// Die Methode verwendet die Aes-Kryptografieklasse, um den Text zu verschlüsseln.
    /// 
    /// </summary>
    public class AesEncryption
    {



        //////////////////////////////////////////////// //part1  eigene key vervenden  für Aes   ////////////////////////////////////////////////////////

        // Setze den Schlüssel und den Initialisierungsvektor
        byte[] key = new byte[] { 0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F };
        byte[] iv = new byte[] { 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F };

        //////////////////////////////////////////////// // eigene key vervenden beendet part1 für Aes ///////////////////////////////////////////////////////
        /// <summary>
        /// 
        /// </summary>
        /// <param name="plainText"></param>
        /// <param name="key"></param>
        /// <param name="plainData"></param>
        /// <param name="iv"></param>
        /// <returns></returns>
        /// 






        public static byte[] Encrypt(byte[] plainText, byte[] key, char plainData,  byte[] iv)
        {  
            /*
                Um die Parameter für den Verschlüsselungs- oder Entschlüsselungsvorgang zu konfigurieren,
                müssen Sie verschiedene Eigenschaften der Kryptografieklasse festlegen, die Sie verwenden. 
                Hier sind einige Beispiele für die Konfiguration von Aes und RSACryptoServiceProvider:
             */
            // Hier setzen wir die Schlüssellänge auf 256 Bits, die Blockgröße auf 128 Bits und verwenden den Padding-Modus PKCS7 und den Cipher-Modus CBC.
            // Erstelle ein neues Aes-Objekt
            Aes aes = Aes.Create();
            aes.KeySize = 256;
            aes.BlockSize = 128;
            aes.Padding = PaddingMode.PKCS7;
            aes.Mode = CipherMode.CBC;

 //////////////////////////////////////////////// // eigene key vervenden ////////////////////////////////////////////////////////
            aes.Key = key;
            aes.IV = iv;
            // Konfiguriere weitere Parameter
            aes.Mode = CipherMode.CBC;
            aes.Padding = PaddingMode.PKCS7;
            // Verwende das Aes-Objekt zur Verschlüsselung und Entschlüsselung


//////////////////////////////////////////////// // eigene key vervenden  hier wird  beendet ////////////////////////////////////////////////////////



            /*
               Generieren Sie einen Schlüssel und einen Initialisierungsvektor (IV) für den AES-Algorithmus
               oder generieren Sie ein Schlüsselpaar für den RSA-Algorithmus.
            */
            aes.GenerateKey(); // Schlüssel generieren
            aes.GenerateIV(); // Initialisierungsvektor generieren
            /*
               Um einen Schlüssel und einen Initialisierungsvektor für den [AES-Algorithmus] zu generieren,
               können Sie die Aes.Create()-Methode verwenden, um eine Instanz der Aes-Klasse zu erstellen,
               und dann die GenerateKey()- und GenerateIV()-Methoden aufrufen:
            */







            /* 
                Um die Daten zu verschlüsseln, können Sie die Encrypt-Methode des Aes-Objekts oder 
                die Encrypt-Methode des RSACryptoServiceProvider-Objekts verwenden, je nachdem welchen Algorithmus Sie verwenden.
                //Für den Aes-Algorithmus würde der Code etwa so aussehen:// 
             */
            // 1- Encrypt für RSA verschlusselung 
            byte[] encryptedData;
            using Aes aesAlg = Aes.Create();
            aesAlg.Key = key;
            aesAlg.IV = iv;
            // Konfigurieren der Parameter
            aes.Mode = CipherMode.CBC;
            aes.Padding = PaddingMode.PKCS7;

            // Erstellen des Encryptors  
            ICryptoTransform encryptor2 = aes.CreateEncryptor();

            // Verschlüsseln der Daten
            using (MemoryStream msEncrypt = new MemoryStream())
            {
                using (CryptoStream csEncrypt = new CryptoStream(msEncrypt, encryptor2, CryptoStreamMode.Write))
                {
                    using (StreamWriter swEncrypt = new StreamWriter(csEncrypt))
                    {
                        // Schreiben der Daten in den CryptoStream
                        swEncrypt.Write(plainData);
                    }
                    encryptedData = msEncrypt.ToArray();
                }

            }








            ICryptoTransform encryptor = aesAlg.CreateEncryptor(aesAlg.Key, aesAlg.IV);

            byte[] cipherText;

            using (var msEncrypt = new System.IO.MemoryStream())
            {
                using (var csEncrypt = new CryptoStream(msEncrypt, encryptor, CryptoStreamMode.Write))
                {
                    using (var swEncrypt = new System.IO.StreamWriter(csEncrypt))
                    {
                        swEncrypt.Write(plainText);
                    }
                    cipherText = msEncrypt.ToArray();
                }
            }

            return cipherText;
        }
    }







    /// <summary>
    /// 
    /// Die Klasse [CryptoService] enthält zwei Methoden, Encrypt() und Decrypt(),
    /// <br />
    /// die einen Byte-Array mit dem Klartext, einem Schlüssel und einem Initialisierungsvektor (IV) 
    /// <br />
    /// als Parameter akzeptieren und den verschlüsselten bzw. entschlüsselten Text zurückgeben. 
    /// <br />
    /// Die Klasse akzeptiert eine Instanz der SymmetricAlgorithm-Klasse im Konstruktor, so dass Sie 
    /// <br />
    /// entweder die Aes-Klasse oder die Rijndael-Klasse verwenden können, um den Text zu verschlüsseln oder zu ents.
    /// 
    /// <param name="">Feri geh nach Hause</param>
    /// 
    /// ES ZEIGTE die   eingabe von returns
    /// <returns>Die Summe von a und b.</returns>
    /// 
    /// </summary>
    public class CryptoService
    {
        private SymmetricAlgorithm _algorithm;

        public CryptoService(SymmetricAlgorithm algorithm)
        {
            _algorithm = algorithm;
        }



        // 1- Encrypt für RSA verschlusselung 
        public byte[] Encrypt(byte[] plainText, byte[] key, byte[] iv, byte[] plainData)
        {

            byte[] encryptedData;







            /*
               Um die Parameter für den Verschlüsselungs- oder Entschlüsselungsvorgang zu konfigurieren,
               müssen Sie verschiedene Eigenschaften der Kryptografieklasse festlegen, die Sie verwenden. 
               Hier sind einige Beispiele für die Konfiguration von Aes und RSACryptoServiceProvider:
            */

            RSACryptoServiceProvider rsa = new RSACryptoServiceProvider();
                rsa.KeySize = 2048;
            /*
               /// Hier setzen wir die Schlüssellänge auf 2048 Bits.///
               Natürlich hängen die Parameter, die Sie konfigurieren müssen, von der spezifischen Anwendung ab.
               Es ist wichtig, sorgfältig zu überlegen, welche Parameter für Ihre Anwendung geeignet sind,
               um die beste Sicherheit und Leistung zu erreichen.
            */






           //////////////////////////////////////////////// // eigene key vervenden ////////////////////////////////////////////////////////

            // Define the key pair
            RSAParameters keyPair = new RSAParameters();

           // rsa.ImportParameters(keyPair.Public); // Verwenden Sie hier Ihren eigenen Schlüsselpaar
                                                  // Erstelle einen neuen RSA-Schlüssel mit einer Schlüssellänge von 2048 Bits
            RSACryptoServiceProvider rsa3 = new RSACryptoServiceProvider(2048);
            // Speichere den öffentlichen Schlüssel in einem Byte-Array
            byte[] publicKey = rsa.ExportRSAPublicKey();
            // Speichere den privaten Schlüssel in einem Byte-Array
            byte[] privateKey = rsa.ExportRSAPrivateKey();

            // Erstelle einen neuen RSACryptoServiceProvider und lade das zuvor erstellte Schlüsselpaar
            RSACryptoServiceProvider rsa2 = new RSACryptoServiceProvider();
            RSAParameters publicKeyParams = new RSAParameters();
            publicKeyParams.Modulus = rsa.ExportParameters(false).Modulus;
            publicKeyParams.Exponent = rsa.ExportParameters(false).Exponent;
            rsa2.ImportParameters(publicKeyParams);

            RSAParameters privateKeyParams = new RSAParameters();
            privateKeyParams.Modulus = rsa.ExportParameters(true).Modulus;
            privateKeyParams.Exponent = rsa.ExportParameters(true).Exponent;
            privateKeyParams.D = rsa.ExportParameters(true).D;
            privateKeyParams.P = rsa.ExportParameters(true).P;
            privateKeyParams.Q = rsa.ExportParameters(true).Q;
            privateKeyParams.DP = rsa.ExportParameters(true).DP;
            privateKeyParams.DQ = rsa.ExportParameters(true).DQ;
            rsa2.ImportParameters(privateKeyParams);

            // Verwende rsa2 zur Verschlüsselung und Entschlüsselung
            // Verschlüsseln der Daten
            encryptedData = rsa.Encrypt(plainData, true);
            /*  
                Um ein Schlüsselpaar für den RSA-Algorithmus zu generieren,
                können Sie die RSACryptoServiceProvider.Create()-Methode verwenden,
                um eine Instanz der RSACryptoServiceProvider-Klasse zu erstellen, 
                und dann die ExportParameters()-Methode aufrufen,
                um die öffentlichen und privaten Schlüssel zu erhalten:
             */





            //////////////////////////////////////////////// // eigene key vervenden bis hier  endet  ////////////////////////////////////////////////////////




            _algorithm.Key = key;
            _algorithm.IV = iv;

            ICryptoTransform encryptor = _algorithm.CreateEncryptor(_algorithm.Key, _algorithm.IV);

            byte[] cipherText;

            using (var msEncrypt = new System.IO.MemoryStream())
            {
                using (var csEncrypt = new CryptoStream(msEncrypt, encryptor, CryptoStreamMode.Write))
                {
                    using (var swEncrypt = new System.IO.StreamWriter(csEncrypt))
                    {
                        swEncrypt.Write(plainText);
                    }
                    cipherText = msEncrypt.ToArray();
                }
            }

            return cipherText;
        }




        // 2- Decrypt für RSA verschlusselung 
        public byte[] Decrypt(byte[] cipherText, byte[] key, byte[] iv)
        {
            /*
               Um die Parameter für den Verschlüsselungs- oder Entschlüsselungsvorgang zu konfigurieren,
               müssen Sie verschiedene Eigenschaften der Kryptografieklasse festlegen, die Sie verwenden. 
               Hier sind einige Beispiele für die Konfiguration von Aes und RSACryptoServiceProvider:
            */
            RSACryptoServiceProvider rsa = new RSACryptoServiceProvider();
            rsa.KeySize = 2048;
            /*
               // Hier setzen wir die Schlüssellänge auf 2048 Bits.//
               Natürlich hängen die Parameter, die Sie konfigurieren müssen, von der spezifischen Anwendung ab.
               Es ist wichtig, sorgfältig zu überlegen, welche Parameter für Ihre Anwendung geeignet sind,
               um die beste Sicherheit und Leistung zu erreichen.
            */





            /*  
                Um ein Schlüsselpaar für den RSA-Algorithmus zu generieren,
                können Sie die RSACryptoServiceProvider.Create()-Methode verwenden,
                um eine Instanz der RSACryptoServiceProvider-Klasse zu erstellen, 
                und dann die ExportParameters()-Methode aufrufen,
                um die öffentlichen und privaten Schlüssel zu erhalten:
             */
            RSAParameters publicKey = rsa.ExportParameters(false); // Öffentlicher Schlüssel
            RSAParameters privateKey = rsa.ExportParameters(true); // Privater Schlüssel


            

            _algorithm.Key = key;
            _algorithm.IV = iv;

            ICryptoTransform decryptor = _algorithm.CreateDecryptor(_algorithm.Key, _algorithm.IV);

            byte[] plainText;

            using (var msDecrypt = new System.IO.MemoryStream(cipherText))
            {
                using (var csDecrypt = new CryptoStream(msDecrypt, decryptor, CryptoStreamMode.Read))
                {
                    using (var srDecrypt = new System.IO.StreamReader(csDecrypt))
                    {
                        plainText = System.Text.Encoding.UTF8.GetBytes(srDecrypt.ReadToEnd());
                    }
                }
            }

            return plainText;
        }


    }




}