using System;
using Microsoft.Maui;
using Microsoft.Maui.Hosting;

namespace _2023_04_28_14_04_Fr_Hello_World;

class Program : MauiApplication
{
	protected override MauiApp CreateMauiApp() => MauiProgram.CreateMauiApp();

	static void Main(string[] args)
	{
		var app = new Program();
		app.Run(args);
	}
}
