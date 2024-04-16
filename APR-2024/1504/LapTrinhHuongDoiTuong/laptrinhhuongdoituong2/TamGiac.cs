using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laptrinhhuongdoituong2
{
    internal class TamGiac
    {
        //thành phần dữ liệu
        private Diem _a;
        private Diem _b;
        private Diem _c;
        private static int _soLuongDoiTuong = 0;

        //thành phần xử lý
        public TamGiac()
        {
            //constructor
            _a = new Diem(0, 1);
            _b = new Diem(0, 0);
            _c = new Diem(1, 0);
            _soLuongDoiTuong++;
        }

        public static bool KiemTraTamGiac(Diem a, Diem b, Diem c)
        {
            double canhA, canhB, canhC;
            canhA = b.TinhKhoangCach(c);
            canhB = c.TinhKhoangCach(a);
            canhC = a.TinhKhoangCach(b);
            return canhA + canhB > canhC &&
                canhC + canhB > canhA &&
                canhA + canhC > canhB;
        }
        public TamGiac(Diem a, Diem b, Diem c)
        {
            if (!TamGiac.KiemTraTamGiac(a, b, c))
            {
                throw new Exception("Tam giac khong hop le.");
            }
            //như thế này thì không kiểm tra được tính hợp lệ, nên sẽ thêm phần trên
            _a = a;
            _b = b;
            _c = c;
            _soLuongDoiTuong++;
        }

        public static int DemSoLuongDoiTuong()
        {
            return _soLuongDoiTuong;
        }


        public void Nhap(string ghiChu)
        {
            Console.WriteLine(ghiChu);
            _a = new Diem();
            _a.Nhap("Nhap đinh A");

            _b = new Diem();
            _b.Nhap("Nhap đinh B");

            _c = new Diem();
            _c.Nhap("Nhap đinh C");
        }

        public double TinhChuVi()
        {
            double a, b, c;
            a = _b.TinhKhoangCach(_c);
            b = _a.TinhKhoangCach(_c);
            c = _a.TinhKhoangCach(_b);
            return a + b + c;
        }

    }
}
