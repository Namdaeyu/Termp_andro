#include<iostream>
#include<string>
#include<fstream>
#include<locale>
#include<clocale>
#include<codecvt>
#include<cstring>
using namespace std;
wstring str[30000];
enum { AA, AB, AC, AD, AE, AF, AG};
int main(){
	int j,k,num=1;
	string folder[] ={"AA","AB","AC","AD","AE","AF","AG"}; //폴더 지정 
	string file_name; //불러올 파일 이름 
	string read_location1 = "G:\\wiki\\text2\\"; // readFile_위치1 
	string write_location1 = "G:\\wiki\\text3\\"; // writeFile_위치1 
	string location3 = "\\wiki_"; //위치3 
	string location5 = ".txt"; //위치5 
	wstring break_string = L"</doc>"; //</doc>가 나오면 다음 주제가 나옴
	string location4;
	for(int fold=0; fold<=AG; fold++){
		string location2(folder[fold]);//위치2 
		for(int i=0; i<100; i++){
			
			if(i<10) location4=("0"+to_string(i));	//위치4(파일이 wiki_0x.txt)형식 
			else location4=(to_string(i));	//위치4 
			
			file_name = read_location1+location2+location3+location4+location5;
			//파일을 읽기 위한 파일 이름 설정 
			wifstream in(file_name);
			in.imbue(locale(locale::empty(),new codecvt_utf8<wchar_t,0x10ffff,consume_header>));
			//파일을 utf-8형태로 사용
			for(k=0;k<30000;k++){
				str[k] = L"none";	//wiki_xx 텍스트를 저장할 string 초기화 
			}
						
			k=0;
			while(getline(in,str[k])){
				k++;
			}
			
			wofstream wof;
			wof.imbue(locale(locale::empty(), new codecvt_utf8<wchar_t, 0x10ffff, generate_header>));
			j=0;
			
			while(j<=k){
				
				string location4(to_string(num));
				file_name=write_location1+location4+location5;	//파일을 쓰기 위한 파일 이름 설정
				wof.open(file_name);
				
				for(j;j<=k;j++){
					if (str[j].compare(break_string) == 0) {
						num++;
						wof.close();
						break;
					}
					
					if (str[j].length() == 0) continue; //공백라인이면 length==0이므로 continue
					
					while (str[j].length() != 0  && str[j].back() == ' ' ) {
						str[j].pop_back();
					}
					if (str[j].length() == 0) continue; //공백라인이면 length==0이므로 continue
					if(str[j].back() != '.' ){ 	//만약 .로 끝나지 않으면 무시하고 continue
						continue;
					}

					wof << str[j]; // 전체 파일을 한 줄로 출력
				}
				j++;
			}
		}
	}
	return 0;
}


