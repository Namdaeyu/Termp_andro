#include<iostream>
#include<string>
#include<fstream>
#include<locale>
#include<clocale>
#include<codecvt>
#include<cstring>
std::wstring str[30000];
enum { AA, AB, AC, AD, AE, AF, AG};
int main(){
	int j,k,num=1;
	std::string folder[] ={"AA","AB","AC","AD","AE","AF","AG"}; //���� ���� 
	std::string file_name; //�ҷ��� ���� �̸� 
	std::string read_location1 = "G:\\wiki\\text2\\"; // readFile_��ġ1 
	std::string write_location1 = "G:\\wiki\\text3\\"; // writeFile_��ġ1 
	std::string location3 = "\\wiki_"; //��ġ3 
	std::string location5 = ".txt"; //��ġ5 
	std::wstring break_string = L"</doc>"; //</doc>�� ������ ���� ������ ����
	std::string location4;
	for(int fold=0; fold<=AG; fold++){
		std::string location2(folder[fold]);//��ġ2 
		for(int i=0; i<100; i++){
			
			if(i<10) location4=("0"+std::to_string(i));	//��ġ4(������ wiki_0x.txt)���� 
			else location4=(std::to_string(i));	//��ġ4 
			
			file_name = read_location1+location2+location3+location4+location5;
			//������ �б� ���� ���� �̸� ���� 
			std::wifstream in(file_name);
			in.imbue(std::locale(std::locale::empty(),new std::codecvt_utf8<wchar_t,0x10ffff,std::consume_header>));
			//������ utf-8���·� ���
			for(k=0;k<30000;k++){
				str[k] = L"none";	//wiki_xx �ؽ�Ʈ�� ������ string �ʱ�ȭ 
			}
						
			k=0;
			while(getline(in,str[k])){
				k++;
			}
			
			std::wofstream wof;
			wof.imbue(std::locale(std::locale::empty(), new std::codecvt_utf8<wchar_t, 0x10ffff, std::generate_header>));
			j=0;
			
			while(j<=k){
				
				std::string location4(std::to_string(num));
				file_name=write_location1+location4+location5;	//������ ���� ���� ���� �̸� ����
				wof.open(file_name);
				
				for(j;j<=k;j++){
					if (str[j].compare(break_string) == 0) {
						num++;
						wof.close();
						break;
					}
					
					if (str[j].length() == 0) continue; //��������̸� length==0�̹Ƿ� continue
					
					while (str[j].length() != 0  && str[j].back() == ' ' ) {
						str[j].pop_back();
					}
					if (str[j].length() == 0) continue; //��������̸� length==0�̹Ƿ� continue
					if(str[j].back() != '.' ){ 	//���� .�� ������ ������ �����ϰ� continue
						continue;
					}

					wof << str[j]; // ��ü ������ �� �ٷ� ���
				}
				j++;
			}
		}
	}
	return 0;
}

