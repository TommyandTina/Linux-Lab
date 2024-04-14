using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laptrinhhuongdoituong4_HinhTron_HinhChuNhat
{
    internal class HinhChuNhat : Hinh
    {
        public Diem A { get; set; }
        public double ChieuDai { get; set; }
        public double ChieuRong { get; set; }

        public override void Nhap(string ghiChu)
        {
            base.Nhap(ghiChu);
            A = new Diem();
            A.Nhap("Nhap dinh A: ");
            Console.Write("Nhap chieu dai :");
            ChieuDai = double.Parse(Console.ReadLine());
            Console.Write("Nhap chieu rong :");
            ChieuRong = double.Parse(Console.ReadLine());
        }
        public override double TinhChuVi()
        {
            return 2 * (ChieuRong + ChieuDai);
        }
    }
}
