
//Question link https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3430/
class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode *temp = head;
        stack<ListNode*> s;
        int len = 0;
        while(temp)
        {
            s.push(temp);
            temp = temp->next;
            len++;
        }

        temp = head;
        ListNode *ans = temp;

        for(int i = 0; i < len; i++)
        {
            if(i % 2 == 0)
            {
                ListNode *element = s.top();
                s.pop();
                if(temp->next!=NULL)
                element->next = temp->next;
                temp->next = element;
            }

            temp = temp->next;
        }
        if(temp!=NULL)
       temp->next = NULL;
        head = ans;
    }
};
