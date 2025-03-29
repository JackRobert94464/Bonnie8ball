using Magic8BallDashboard.Services;

var builder = WebApplication.CreateBuilder(args);

// Add MVC services with Razor runtime compilation
builder.Services.AddControllersWithViews().AddRazorRuntimeCompilation();

// Register Magic8BallService
builder.Services.AddSingleton<Magic8BallService>();

var app = builder.Build();

// Configure HTTP request pipeline
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();
}

app.UseStaticFiles();
app.UseRouting();

app.UseEndpoints(endpoints =>
{
    endpoints.MapControllerRoute(
        name: "default",
        pattern: "{controller=Magic8Ball}/{action=Index}/{id?}");
});

app.Run();
