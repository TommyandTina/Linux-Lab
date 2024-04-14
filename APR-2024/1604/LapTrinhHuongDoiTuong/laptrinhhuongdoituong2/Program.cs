using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laptrinhhuongdoituong2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            TamGiac tg;
            try
            {
                tg = new TamGiac(new Diem(0, 0), new Diem(1, 1), new Diem(2, 0));
                Console.WriteLine("So luong doi tuong hien tai la: " + TamGiac.DemSoLuongDoiTuong());
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                return;
            }

            //Nhập thông tin tam giác
            //tg.Nhap("Nhap tam giác");

            //Yêu cầu đối tượng tính chu vi
            double kq = tg.TinhChuVi();
            string chuoi = "Ket qua là " + kq;
            Console.WriteLine(chuoi);



            /*
            LopPhanSo p1;
            p1 = new LopPhanSo();
            //p1.TuSo = 1;
            //p1.MauSo = 2;
            int m = p1.MauSo;
            Console.WriteLine(p1.XuatPhanSo());
            */
        }
    }
}
