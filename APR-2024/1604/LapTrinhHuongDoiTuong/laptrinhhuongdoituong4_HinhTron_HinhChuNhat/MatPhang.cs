using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laptrinhhuongdoituong4_HinhTron_HinhChuNhat
{
    internal class TaoLapHinh
    {
        public static Hinh TaoDoiTuongHinh(int loai)
        {
            if (loai == 1)
            {
                return new HinhTron();
            }
            else
            {
                return new HinhChuNhat();
            }
        }

    }
    internal class CongTy
    {
        //thành phần dữ liệu
        private string _ten;
        private Hinh[] _dsHinh;


        //thành phần xử lý
        public void Nhap(string ghiChu)
        {
            Console.WriteLine(ghiChu);
            Console.Write("Nhap ten mat phang: ");
            _ten = Console.ReadLine();
            Console.Write("Nhap so luong hinh : ");
            int n = int.Parse(Console.ReadLine());

            _dsHinh = new Hinh[n];
            for (int i = 0; i < _dsHinh.Length; i++)
            {
                Console.Write("1. Tron 2.HCN");
                int loai = int.Parse(Console.ReadLine());
                _dsHinh[i] = TaoLapHinh.TaoDoiTuongHinh(loai);
                _dsHinh[i].Nhap($"Nhap thong tin hinh thu {i + 1}: ");
            }
        }

        public double TinhTongChuVi()
        {
            double s = 0;
            for (int i = 0; i < _dsHinh.Length; i++)
            {
                s = s + _dsHinh[i].TinhChuVi();
            }


            return s;
        }

    }
}
