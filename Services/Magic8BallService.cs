using System.Diagnostics;
using System.IO;

namespace Magic8BallDashboard.Services
{
    public class Magic8BallService
    {
        public string GetMysticalAnswer(string question)
        {
            string pythonPath = "python";  // Ensure Python is installed and available in PATH
            string scriptPath = Path.Combine(Directory.GetCurrentDirectory(), "PythonModule/mystic_answers.py");

            ProcessStartInfo start = new ProcessStartInfo()
            {
                FileName = pythonPath,
                Arguments = $"\"{scriptPath}\" \"{question}\"",
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                CreateNoWindow = true,
                UseShellExecute = false
            };

            string result;
            using (Process process = Process.Start(start))
            {
                result = process.StandardOutput.ReadToEnd().Trim();
                process.WaitForExit();
            }

            return result;
        }
    }
}
