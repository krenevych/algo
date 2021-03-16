#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#endif

#include<iostream>

using namespace std;

static int testNum;

class PrefixTree {

public:
	PrefixTree()
		: leaf(false)
	{
		init();
	}

	void init() {
		for (int i = 0; i < 10; i++) {
			children[i] = 0;
		}
	}

	bool hasChildren() {
		for (int i = 0; i < 10; i++) {
			if (children[i] != 0) return true;
		}
		return false;
	}

	bool add(char* branch) {
		PrefixTree* curr = this;
		char* c = branch;
		while (*c != 0) {
			if (curr->leaf)
				return false;

			int key = *c - '0';
			if (curr->children[key] == 0) {
				curr->children[key] = new PrefixTree();
			}

			curr = curr->children[key];
			c++;
		}

		if (curr->leaf || curr->hasChildren()) {
			return false;
		}

		curr->leaf = true;
		return true;
	}

private:
	bool leaf;
	PrefixTree* children[10];
};

int main() {
    freopen("input.txt", "r", stdin);

    scanf("%d", &testNum);
    for (int i = 0; i < testNum; ++i) {
		PrefixTree book;
		int phonesNum;
		bool res = true;
        scanf("%d", &phonesNum);
        for (int ph = 0; ph < phonesNum; ++ph) {

            char phone[11];
            scanf("%s", &phone);
			if (!res) continue;
			res = book.add(phone);
        }

		if (res)
			printf("YES\n");
		else
			printf("NO\n");

    }
    return 0;
}