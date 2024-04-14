using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laptrinhhuongdoituong3_tinhkethua
{
    internal class NhanVienSanXuat : NhanVien
    {
        private double _soSanPham;
        public double SoSanPham
        {
            get { return _soSanPham; }
            set 
            {
                if (value >=0 )
                    _soSanPham = value;
            }
        }


        public override void Nhap(string ghiChu)
        {
            base.Nhap(ghiChu);
            Console.Write("Nhap so san pham : ");
            SoSanPham = double.Parse(Console.ReadLine());
        }

        public override double TinhLuong()
        {
            return SoSanPham * 100;
        }
    }
}
