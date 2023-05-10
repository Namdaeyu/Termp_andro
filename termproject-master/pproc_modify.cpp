#include<iostream>
#include<string>
#include<fstream>
#include<locale>
#include<clocale>
#include<codecvt>
#include<cstring>
using namespace std;
wstring str[30000];
enum { AA, AB, AC, AD, AE, AF, AG };
int main() {
	int j, k, num = 1;
	string folder[] = { "AA","AB","AC","AD","AE","AF","AG" }; //���� ���� 
	string file_name; //�ҷ��� ���� �̸� 
	string read_location1 = "G:\\wiki\\text2\\"; // readFile_��ġ1 
	string write_location1 = "G:\\wiki\\dataset\\"; // writeFile_��ġ1 
	string location3 = "\\wiki_"; //��ġ3 
	string location5 = ".txt"; //��ġ5 
	wstring break_string = L"</doc>"; //</doc>�� ������ ���� ������ ����
	string location4;
	for (int fold = 0; fold <= AG; fold++) {
		string location2(folder[fold]);//��ġ2 
		string location4("wiki" + to_string(num));
		file_name = write_location1 + location4 + location5;	//������ ���� ���� ���� �̸� ����
		wofstream wof;
		wof.imbue(locale(locale::empty(), new codecvt_utf8<wchar_t, 0x10ffff, generate_header>));
		wof.open(file_name);
		for (int i = 0; i < 100; i++) {

			if (i < 10) location4 = ("0" + to_string(i));	//��ġ4(������ wiki_0x.txt)���� 
			else location4 = (to_string(i));	//��ġ4 

			file_name = read_location1 + location2 + location3 + location4 + location5; //������ �б� ���� ���� �̸� ���� 
			wifstream in(file_name);
			in.imbue(locale(locale::empty(), new codecvt_utf8<wchar_t, 0x10ffff, consume_header>)); //������ utf-8���·� ���
			for (k = 0; k < 30000; k++) {
				str[k] = L"none";	//wiki_xx �ؽ�Ʈ�� ������ string �ʱ�ȭ 
			}

			k = 0;
			while (getline(in, str[k])) { k++; }

			for (j = 0; j <= k; j++) {
				for (j; j <= k; j++) {
					if (str[j].compare(break_string) == 0) break;

					if (str[j].length() == 0) continue; //��������̸� length==0�̹Ƿ� continue

					while (str[j].length() != 0 && str[j].back() == ' ') {
						str[j].pop_back();
					}
					if (str[j].length() == 0) continue; //��������̸� length==0�̹Ƿ� continue
					if (str[j].back() != '.') continue; //���� .�� ������ ������ �����ϰ� continue
					wof << str[j]; // ��ü ������ �� �ٷ� ���, �����ٷ�
				}
				wof << std::endl;
			}
		}
		num++;
		wof.close();
	}
	return 0;
}
