def find_all_word_paths_dfs(start_word, target_word, word_list):
    word_pool = set(word_list)
    if target_word not in word_pool:
        return []

    final_results = []
    active_path_words = {start_word}

    def explore_paths(current_word, current_path):
        if current_word == target_word:
            final_results.append(list(current_path))
            return

        for position in range(len(current_word)):
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                new_word = current_word[:position] + letter + current_word[position+1:]

                if new_word in word_pool and new_word not in active_path_words:
                    active_path_words.add(new_word)
                    explore_paths(new_word, current_path + [new_word])
                    active_path_words.remove(new_word)

    explore_paths(start_word, [start_word])
    return final_results

# Example execution
print(find_all_word_paths_dfs("hit", "cog", ["hot","dot","dog","lot","log","cog"]))