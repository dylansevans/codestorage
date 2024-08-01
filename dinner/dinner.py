from itertools import permutations

def find_dislikes(friends: dict)->set[tuple[str]]:
    """Given a dictionary-based adjacency list of String-based nodes,
       returns a set of all edges in the graph (ie. dislikes who can't be invited together).
       
       Args:
           friends: dictionary-based adjacency matrix representing friend relations
       
       Returns:
           A set of edges in the graph represented as tuples
            - An edge should only appear once in the set.
            - Each edge should list node connections in alphabetical order.

       Example
       -------
       >>> friends={'Alice':['Bob'],'Bob':['Alice', 'Eve'],'Eve':['Bob']}
       >>> find_dislikes(friends)
       {('Alice', 'Bob'), ('Bob', 'Eve')}

    """
    ### BEGIN SOLUTION
    set_to_return = set()
    for person in friends.keys():
        for opp in friends[person]:
            set_to_return.add(tuple(sorted([person, opp])))

    return set_to_return
    ### END SOLUTION

def filter_no_dislikes(friends:dict)->tuple[list[str], dict]:
    '''An optimization that removes friends who are not in any dislikes relationships,
       prior to generating combinations and add them to the invite list.

       Args:
           friends: dictionary-based adjacency matrix representing friend relations
       
       Returns:
           A tuple containing:
            - list of friends not in dislike relations AND 
            - resulting dictionary with these friends removed

       Example
       -------
       >>> friends={'Alice':['Bob'],'Bob':['Alice', 'Eve'],'Cleo':[],'Don':[],'Eve':['Bob']}
       >>> filter_no_dislikes(friends)
       (['Cleo', 'Don'], {'Alice': ['Bob'], 'Bob': ['Alice', 'Eve'], 'Eve': ['Bob']})
    '''
    ### BEGIN SOLUTION
    no_opps = []
    fiendish_fellas = {}
    for person in friends.keys():
        if len(friends[person]) == 0:
            no_opps.append(person)
        else:
            fiendish_fellas[person] = friends[person]

    return no_opps, fiendish_fellas
    ### END SOLUTION

def filter_bad_invites(all_subsets:list, friends:dict)->list[list[str]]:
    '''Removes subsets from all_subsets that contain any pair of friends who
       are in a dislike relationship

       Args:
           all_subsets: a list of all possible friend combinations, each reresented as a list of strings
           friends: dictionary-based adjacency matrix representing friend relations
       
       Returns:
           A list containing only friend combinations that exclude dislike pairs
      
       Example
       -------
       >>> all_subsets = [[], ['Eve'], ['Bob'], ['Bob', 'Eve'], ['Alice'], ['Alice', 'Eve'], ['Alice', 'Bob'], ['Alice', 'Bob', 'Eve']]
       >>> friends={'Alice':['Bob'],'Bob':['Alice'],'Eve':[]} 
       >>> filter_bad_invites(all_subsets, friends)
       [[], ['Eve'], ['Bob'], ['Bob', 'Eve'], ['Alice'], ['Alice', 'Eve']]
    '''
    ### BEGIN SOLUTION
    good_invites = []

    for subset in all_subsets:
        rule_breaker = False
        for person in subset:
            # the variable person referring to a person possible invite list
            for opp in friends[person]:
                if opp in subset:
                    rule_breaker = True
        if not rule_breaker: good_invites.append(subset)
    
    return good_invites
    ### END SOLUTION

def invite_to_dinner_optimized(friends:dict)->list[str]:
    '''Finds the combination with the maximum number of guests without storing all subset combinations

       Functions the same as invite_to_dinner_better. However, your solution should not call the 
       function generate_all_subsets. Instead, you should integrate the generation of subsets with the process of
       finding the maximum number of guests so that you can reduce the overall memory footprint of your algorithm.
       
       Args:
           friends: dictionary-based adjacency matrix representing friend relations
       
       Returns:
           A set of friends to invite to dinner which maximizes the number of friends on the list
       
       Example
       -------
       >>> friends={'Alice':['Bob'],'Bob':['Alice', 'Eve'],'Cleo':[],'Don':[],'Eve':['Bob']}
       >>> invite_to_dinner_optimized(friends)
       ['Alice', 'Eve', 'Cleo', 'Don']
    '''
    ### BEGIN SOLUTION
    good_invites = []

    friend_list = list(friends.keys())
    n = len(friends)
    
    for i in range(2**n):
        num = i  #convert each number in the range to a binary string
        new_subset = []
        for j in range(n): # to_binary_division approach
            if (num % 2 == 1): # 1 indicates the guest is included
                new_subset = [friend_list[n-1-j]] + new_subset 
            num = num // 2
        if determine_if_valid(new_subset, friends):
            good_invites.append(new_subset)

    best = []
    longest = 0
    for valid in good_invites:
        if len(valid) > longest:
            best = valid
            longest = len(valid)
    return sorted(list(best))
    ### END SOLUTION

def determine_if_valid(attempted_set, friends):
    for person in attempted_set:
        for opp in friends[person]:
            if opp in attempted_set:
                return False  
    return True

def generate_all_subsets(friends: dict)->list[list[str]]:
    '''Converts each number from 0 to 2^n - 1 into binary and uses the binary representation
       to determine the combination of guests and returns all possible combinations
      
       Args:
           friends: dictionary-based adjacency matrix representing friend relations
       
       Returns:
           A list of all possible subsets of friends to invite, represented as lists of strings
       
       Example
       -------
       >>> friends={'Alice':['Bob'],'Bob':['Alice', 'Eve'],'Eve':['Bob']}
       >>> generate_all_subsets(friends)
       [[], ['Eve'], ['Bob'], ['Bob', 'Eve'], ['Alice'], ['Alice', 'Eve'], ['Alice', 'Bob'], ['Alice', 'Bob', 'Eve']]
    '''
    friend_list = list(friends.keys())
    n = len(friends)
    
    all_subsets = []

    for i in range(2**n):
        num = i  #convert each number in the range to a binary string
        new_subset = []
        for j in range(n): # to_binary_division approach
            if (num % 2 == 1): # 1 indicates the guest is included
                new_subset = [friend_list[n-1-j]] + new_subset 
            num = num // 2
        all_subsets.append(new_subset)

    return all_subsets

def invite_to_dinner_slow(friends: dict)-> list[str]:
    '''Finds the invite combo with the maximum number of guests via the exhaustive approach:
            1. Generate every possible combination of guests
            2. Filter out the combinations that include dislike relationships
            3. Find the combination which give you the maximum number of invites

       Args:
           friends: dictionary-based adjacency matrix representing friend relations
       
       Returns:
           A list of friends to invite to dinner which maximizes the number of friends on the list
       
       Example
       -------
       >>> riends={'Alice':['Bob'],'Bob':['Alice', 'Eve'],'Cleo':[],'Don':[],'Eve':['Bob']}
       >>> invite_to_dinner_slow(friends)
       ['Alice', 'Cleo', 'Don', 'Eve']
    '''
    all_subsets = generate_all_subsets(friends)
    only_good_subsets = filter_bad_invites(all_subsets, friends)

    #find the subset which maximizes number of invites
    invite_list = []
    for i in only_good_subsets:
        if len(i) > len(invite_list):
            invite_list = i

    return invite_list

def invite_to_dinner_better(friends: dict)-> list[str]:
    '''Finds the invite combo with the maximum number of guests
       
       Args:
           friends: dictionary-based adjacency matrix representing friend relations
       
       Returns:
           A list of friends to invite to dinner which maximizes the number of friends on the list
       
       Example
       -------
       >>> friends={'Alice':['Bob'],'Bob':['Alice', 'Eve'],'Cleo':[],'Don':[],'Eve':['Bob']}
       >>> invite_to_dinner_better(friends)
       ['Alice', 'Eve', 'Cleo', 'Don']
    '''
    definite_invites, problem_friends = filter_no_dislikes(friends)
    fewer_subsets = generate_all_subsets(problem_friends) #smaller graph
    only_good_subsets = filter_bad_invites(fewer_subsets, problem_friends)

    #find the subset which maximizes number of invites
    invite_list = []
    for i in only_good_subsets:
        if len(i) > len(invite_list):
            invite_list = i

    #recombine with definite invites in Pythonic fashion
    invite_list += definite_invites

    return invite_list



if __name__ == "__main__":
    friends={
        'Alice':['Bob'],
        'Bob':['Alice', 'Eve'],
        'Cleo':[],
        'Don':[],
        'Eve':['Bob']
    }
    print(invite_to_dinner_slow(friends))
    print(invite_to_dinner_better(friends))
    print(invite_to_dinner_optimized(friends))

    
    friends_2={
        'Alice':['Bob'],
        'Bob':['Alice', 'Eve'],
        'Eve':['Bob']
    }
    print(invite_to_dinner_slow(friends_2))
    print(invite_to_dinner_better(friends_2))
    print(invite_to_dinner_optimized(friends_2))

    friends_3={
        'Asa':[], 
        'Bear':['Cate'],
        'Cate':['Bear', 'Dave'],
        'Dave':['Cate','Eve'], 
        'Eve':['Dave'], 
        'Finn':['Ginny', 'Haruki', 'Ivan'], 
        'Ginny':['Finn','Haruki'], 
        'Haruki':['Ginny', 'Finn'], 
        'Ivan':['Finn']
    }
    print(invite_to_dinner_slow(friends_3))
    print(invite_to_dinner_better(friends_3))
    print(invite_to_dinner_optimized(friends_3))
    