#include <regex>

int main() {
    std::string str;
    while (true) {
        std::cin >> str;
        std::regex e("abc.", regex_constants::icase);
        std::regex c("(abc)de+\\1");
        std::regex f("(ab)c(de+)\\2\\1");
        // using character class
        std::regex w("[[:w:]]+@[[:w:]]+\.com");
        bool match = regex_match(str, e);
        bool match = regex_search(str, e);

        std::cout << (match? "match" : "no match") << std::endl;

    }

    return 0;
}