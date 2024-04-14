using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laptrinhhuongdoituong2
{
    internal class LopPhanSo
    {
        //thành phần thông tin
        private int _mauSo;
        private int _tuSo;

        //hàm tạo
        public LopPhanSo()
        {
            _mauSo = 1;
            _tuSo = 0;
        }

        public LopPhanSo(int n)
        {
            _mauSo = 1;
            _tuSo = n;
        }

        //thành phần xử lý
        public int MauSo
        {
            get
            {
                return _mauSo;
            }
            set
            {
                if (value != 0)
                {
                    _mauSo = value;
                }
            }
        }
        public int TuSo
        {
            get { return _tuSo; }
            set { _tuSo = value; }
        }

        public void NhapPhanSo(string ghiChu)
        {
            Console.WriteLine(ghiChu);
            Console.WriteLine("Nhap tu so::");
            _tuSo = int.Parse(Console.ReadLine());
            Console.WriteLine("Nhap mau so:");
            _mauSo = int.Parse(Console.ReadLine());
        }
        public LopPhanSo CongPS(LopPhanSo p2)
        {
            LopPhanSo kq = new LopPhanSo();
            kq._tuSo = _tuSo * p2._mauSo + _mauSo * 
                p2._tuSo;
            kq._mauSo = _mauSo * p2._mauSo;
            return kq;
        }
        public string XuatPhanSo()
        {
            return $"{_tuSo}/{_mauSo}";
        }
    }
}
