using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laptrinhhuongdoituong3_tinhkethua
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Hello World\n");
            CongTy a = new CongTy();
            a.Nhap("Nhap thong tin cong ty: ");
            double kq = a.TinhTongLuong();
            Console.WriteLine(kq);

            /*            NhanVienSanXuat nvsx = new NhanVienSanXuat("LE VAN A");
                        nvsx.Nhap("Nhap nhan vien san xuat")*/
            ;
        }
    }
}
