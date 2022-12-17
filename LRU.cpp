class LRUCache {
private:
  list<pair<int, int>> cache;
  unordered_map<int, list<pair<int, int>>::iterator> MAP;//�ο���⣬ʹ�õ������������˴����� 
  int Size;

public:
  LRUCache(int capacity) : Size(capacity) {}


int get(int key) {
    if(MAP.find(key) == MAP.end())
		return -1;//�����ڣ�����-1 
    else
    {
        cache.splice(cache.begin(), cache, MAP[key]);//���»����б� ��������ѯ������ǰ 
        return MAP[key]->second;
    }
}

void put(int key, int value) {
    if(get(key) != -1)
		MAP[key]->second = value;//���ڣ���ֵ 
    else    
    {   //�����ڣ��½���� 
        if(cache.size() == Size)//��������ɾ����ǰ��� 
        {
            int del = cache.back().first;
            cache.pop_back();
            MAP.erase(del);
        }
        cache.emplace_front(key, value);//����½ڵ� 
        MAP[key] = cache.begin();
    }
}
};

