
using System;
using System.Drawing;
using System.Windows.Forms;
using System.Net;
using System.IO;

namespace RMDEditor
{
	/// <summary>
	/// Description of FunctionList.
	/// </summary>
	public partial class FunctionList : Form
	{	
		string functions;
		
		public FunctionList()
		{
			InitializeComponent();
			
			if(!File.Exists("FunctionList.txt"))
			{
				WebClient webClient = new WebClient();
				webClient.DownloadFile("http://mysite.com/myfile.txt", @"FunctionList.txt");
			}
			
			else
			{
				functions = File.ReadAllText("FunctionList.txt");
				richTextBox1.Text = functions;
			}
		}
	}
}
