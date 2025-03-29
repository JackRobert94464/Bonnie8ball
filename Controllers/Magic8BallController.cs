using Microsoft.AspNetCore.Mvc;
using Magic8BallDashboard.Services;
using Magic8BallDashboard.Models;

namespace Magic8BallDashboard.Controllers
{
    public class Magic8BallController : Controller
    {
        private readonly Magic8BallService _magic8BallService;

        public Magic8BallController()
        {
            _magic8BallService = new Magic8BallService();
        }

        [HttpGet]
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public JsonResult GetAnswer([FromBody] Magic8BallResult request)
        {
            string answer = _magic8BallService.GetMysticalAnswer(request.Question);
            return Json(new { Answer = answer });
        }
    }
}
