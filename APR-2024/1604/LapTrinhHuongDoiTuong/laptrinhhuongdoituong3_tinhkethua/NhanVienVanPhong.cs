using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laptrinhhuongdoituong3_tinhkethua
{
    internal class NhanVienVanPhong: NhanVien
    {
        private double _heSoLuong;
        private double _phuCap;
        public double HeSoLuong
        {
            get { return _heSoLuong; }
            set 
            {
                if (value >= 1 && value <= 10)
                    _heSoLuong = value;
            }
        }
        public double PhuCap
        {
            get { return _phuCap; }
            set
            {
                if (value >= 1 && value <= 10)
                    _phuCap = value;
            }
        }

        public override void Nhap(string ghiChu)
        {
            base.Nhap(ghiChu);
            Console.Write("Nhap he so luong : ");
            HeSoLuong = double.Parse(Console.ReadLine());
            Console.Write("Nhap phu cap: ");
            PhuCap = double.Parse(Console.ReadLine());
        }

        public override double TinhLuong()
        {
            return HeSoLuong * 1000 + PhuCap;
        }
    }
}
