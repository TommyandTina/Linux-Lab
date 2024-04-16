using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laptrinhhuongdoituong4_HinhTron_HinhChuNhat
{
    public class Hinh
    {
        public string MauSac { get; set; }
        public virtual void Nhap(string ghiChu)
        {
            Console.WriteLine(ghiChu);
            Console.Write("Nhap mau sac");
            MauSac = Console.ReadLine();
        }

        public virtual double TinhChuVi()
        {
            return 0;
        }
    }
}
