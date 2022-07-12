# jc-be

# Read sql
delete FROM public.keyword;

insert into public.keyword (text, text_en, unaccented_text)
values('Kỹ sư phần mềm', 'Software engineer', 'Ky su phan mem');

insert into public.keyword (text, text_en, unaccented_text)
values('Kỹ sư phần mềm C/C++', 'Software engineer C/C++', 'Ky su phan mem C/C++');

insert into public.keyword (text, text_en, unaccented_text)
values('Kỹ sư an ninh thông tin', 'Information security engineer', 'Ky su an ninh thong tin');

insert into public.keyword (text, text_en, unaccented_text)
values('Lập trình viên', 'Programmer', 'Lap trinh vien');

insert into public.keyword (text, text_en, unaccented_text)
values('Quản lý rủi ro', 'Risk manager', 'Quan ly rui ro');

insert into public.keyword (text, text_en, unaccented_text)
values('Nhân viên IT hardware', 'IT hardware support', 'Nhan vien IT hardware');

insert into public.keyword (text, text_en, unaccented_text)
values('Chuyên viên IT', 'IT specialist', 'Chuyen vien IT');

insert into public.keyword (text, text_en, unaccented_text)
values('Chuyên viên công nghệ thông tin', 'IT specialist', 'Chuyen vien cong nghe thong tin');

insert into public.keyword (text, text_en, unaccented_text)
values('Quản lý sản phẩm', 'Product manager', 'Quan ly san pham');

insert into public.keyword (text, text_en, unaccented_text)
values('Chuyên viên SEO', 'SEO specialist',	'Chuyen vien SEO');

insert into public.keyword (text, text_en, unaccented_text)
values('Dịch vụ ứng dụng', 'Application support engineer', 'Dich vu ung dung');

insert into public.keyword (text, text_en, unaccented_text)
values('Quản lý vận hành cơ sở dữ liệu', 'Database manager', 'Quan ly van hanh co so du lieu');

insert into public.keyword (text, text_en, unaccented_text)
values('Quản lý dự án', 'Project manager', 'Quan ly du an');

insert into public.keyword (text, text_en, unaccented_text)
values('Chuyên gia quản lý dự án', 'Project management specialist', 'Chuyen gia quan ly du an');

insert into public.keyword (text, text_en, unaccented_text)
values('Thiết kế UI/UX', 'UI/UX designer', 'Thiet ke UI/UX');

insert into public.keyword (text, text_en, unaccented_text)
values('Kỹ sư kiểm thử phần mềm', 'QA Engineer', 'Ky su kiem thu phan mem');

insert into public.keyword (text, text_en, unaccented_text)
values('Phân tích nghiệp vụ', 'Business Analyst', 'Phan tich nghiep vu');

insert into public.keyword (text, text_en, unaccented_text)
values('Kỹ sư hệ thống', 'System Engineer', 'Ky su he thong');

insert into public.keyword (text, text_en, unaccented_text)
values('Kỹ sư ứng dụng an toàn thông tin', 'Application Security Engineer', 'Ky su ung dung an toan thong tin');

insert into public.keyword (text, text_en, unaccented_text)
values('Thiết kế đồ hoạ', 'Graphic designer', 'Thiet ke do hoa');

insert into public.keyword (text, text_en, unaccented_text)
values('Chuyên viên triển khai phần mềm', 'ERP specialist', 'Chuyen vien trien khai phan mem');

insert into public.keyword (text, text_en, unaccented_text)
values('Chuyên viên đảm bảo an ninh', 'Pentest', 'Chuyen vien dam bao an ninh');

insert into public.keyword (text, text_en, unaccented_text)
values('Chuyên gia kiến trúc công nghệ thông tin', 'Digital Architect Specialist', 'Chuyen gia kien truc cong nghe thong tin');

insert into public.keyword (text, text_en, unaccented_text)
values('Chuyên gia an ninh mạng', 'Network security engineer', 'Chuyen gia an ninh mang');

insert into public.keyword (text, text_en, unaccented_text)
values('Kiến trúc sư nghiệp vụ', 'IT business architect', 'Kien truc su nghiep vu');

insert into public.keyword (text, text_en, unaccented_text)
values('Chuyên viên  triển ứng dụng', 'App developer specialist', 'Chuyen vien  trien ung dung');

insert into public.keyword (text, text_en, unaccented_text)
values('Kỹ sự giải pháp', 'Solution Engineer', 'Ky su giai phap');

insert into public.keyword (text, text_en, unaccented_text)
values('Kỹ sư dữ liệu', 'Data engineer', 'Ky su du lieu');

insert into public.keyword (text, text_en, unaccented_text)
values('Chuyên gia nghiên cứu xử lý ngôn ngữ tự nhiên', 'NLP Researcher', 'Chuyen gia nghien cuu xu ly ngon ngu tu nhien');

insert into public.keyword (text, text_en, unaccented_text)
values('Chuyên viên bán hàng dự án công nghệ thông tin', 'IT Sales person',	'Chuyen vien ban hang du an cong nghe thong tin');

insert into public.keyword (text, text_en, unaccented_text)
values('Chuyên  tư vấn giải pháp và quản lý dự án', 'IT solution and project management consultant', 'Chuyen  tu van giai phap va quan ly du an');

insert into public.keyword (text, text_en, unaccented_text)
values('Chuyên  tư vấn giải pháp và quản lý dự án', 'IT solution and project management consultant', 'Chuyen  tu van giai phap va quan ly du an');

SELECT id, text, text_en, unaccented_text
	FROM public.keyword;