'''
���� ����
�־��� �װ����� ��� �̿��Ͽ� �����θ� ¥���� �մϴ�. �׻� ICN ���׿��� ����մϴ�.

�װ��� ������ ��� 2���� �迭 tickets�� �Ű������� �־��� ��, �湮�ϴ� ���� ��θ� �迭�� ��� return �ϵ��� solution �Լ��� �ۼ����ּ���.

���ѻ���
��� ������ ���ĺ� �빮�� 3���ڷ� �̷�����ϴ�.
�־��� ���� ���� 3�� �̻� 10,000�� �����Դϴ�.
tickets�� �� �� [a, b]�� a ���׿��� b �������� ���� �װ����� �ִٴ� �ǹ��Դϴ�.
�־��� �װ����� ��� ����ؾ� �մϴ�.
���� ������ ��ΰ� 2�� �̻��� ��� ���ĺ� ������ �ռ��� ��θ� return �մϴ�.
��� ���ø� �湮�� �� ���� ���� �־����� �ʽ��ϴ�.

����� ��
tickets	return
[[ICN, JFK], [HND, IAD], [JFK, HND]]	[ICN, JFK, HND, IAD]
[[ICN, SFO], [ICN, ATL], [SFO, ATL], [ATL, ICN], [ATL,SFO]]	[ICN, ATL, ICN, SFO, ATL, SFO]

����� �� ����
���� #1

[ICN, JFK, HND, IAD] ������ �湮�� �� �ֽ��ϴ�.

���� #2

[ICN, SFO, ATL, ICN, ATL, SFO] ������ �湮�� ���� ������ [ICN, ATL, ICN, SFO, ATL, SFO] �� ���ĺ� ������ �ռ��ϴ�.
'''
import copy

def _search(left_tickets, ticket_history, result):
    for ticket in left_tickets:
        if ticket_history[-1][1] == ticket[0]:
            if len(left_tickets) > 1:
                added_history = copy.deepcopy(ticket_history)
                added_history.append(ticket)
                _search(copy.deepcopy([x for x in left_tickets if x is not ticket])
                                , added_history
                                , result)
            elif len(left_tickets) == 1:
                ticket_history.append(ticket)
                result.append(ticket_history)


def solution(tickets):
    answer = []
    result = []
    for ticket in tickets:
        if ticket[0] == 'ICN':
            left_tickets = copy.deepcopy([x for x in tickets if x is not ticket])
            _search(left_tickets, [ticket], result)
    
    for seq in result:
        path = []
        for index, ticket in enumerate(seq):
            if index == 0:
                path.extend(ticket)
            else:
                path.append(ticket[1])
        answer.append(path)
    
    answer = sorted(answer, key = lambda x: x)
    
    return answer[0]