using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laptrinhhuongdoituong4_HinhTron_HinhChuNhat
{
    internal class HinhTron :Hinh
    {
        public Diem Tam { get; set; }
        public double BanKinh { get; set; }

        public override void Nhap(string ghiChu)
        {
            base.Nhap(ghiChu);
            Tam = new Diem();
            Tam.Nhap("Nhap tam hinh tron: ");
            Console.Write("Nhap ban kinh :");
            BanKinh = double.Parse(Console.ReadLine());

        }

        public override double TinhChuVi()
        {
            return 2 * Math.PI * BanKinh;
        }
    }
}
