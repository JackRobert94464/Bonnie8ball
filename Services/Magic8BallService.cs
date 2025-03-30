using System.Diagnostics;
using System.IO;

namespace Magic8BallDashboard.Services
{
    public class Magic8BallService
    {
        public string GetMysticalAnswer(string question)
{
    string pythonPath = "python";  // or "python3"
    string scriptPath = Path.Combine(Directory.GetCurrentDirectory(), "PythonModule", "8ball.py");

    Console.WriteLine("[PATH DEBUG] Trying to run: " + scriptPath);

    var start = new ProcessStartInfo
    {
        FileName = pythonPath,
        Arguments = $"\"{scriptPath}\" \"{question}\"",
        RedirectStandardOutput = true,
        RedirectStandardError = true,
        CreateNoWindow = true,
        UseShellExecute = false
    };

    using (var process = Process.Start(start))
    {
        string output = process?.StandardOutput.ReadToEnd()?.Trim() ?? "";
        string errors = process?.StandardError.ReadToEnd()?.Trim() ?? "";
        process?.WaitForExit();

        if (!string.IsNullOrEmpty(errors))
        {
            Console.WriteLine("[PYTHON ERROR] " + errors);
        }

        if (string.IsNullOrWhiteSpace(output))
        {
            Console.WriteLine("[PYTHON OUTPUT EMPTY]");
            return "The spirits are silent...";
        }

        Console.WriteLine("[PYTHON OUTPUT] " + output);
        return output;
    }
}

    }
}
