using Microsoft.AspNetCore.Mvc;
using Magic8BallDashboard.Models;

namespace Magic8BallDashboard.Controllers
{
    public class WisdomController : Controller
    {
        private static List<Wisdom> _wisdoms = new List<Wisdom>();
        private static int _nextId = 1;

        public IActionResult Index()
        {
            return View(_wisdoms);
        }

        [HttpPost]
        public IActionResult Add(string text)
        {
            if (!string.IsNullOrWhiteSpace(text))
            {
                _wisdoms.Add(new Wisdom { Id = _nextId++, Text = text.Trim() });
            }

            return RedirectToAction("Index");
        }
    }
}
