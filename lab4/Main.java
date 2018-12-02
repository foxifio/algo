public class Main {
    public static int countFriends(String[] friends) {
        String[] ret = new String[friends.length];
        for (int i = 0; i < friends.length; i++) {
            ret[i] = friends[i];
        }

        for (int i = 0; i < friends.length; i++) {
            for (int j = 0; j < friends[i].length(); j++) {
                if (friends[i].charAt(j) == 'Y') {
                    for(int k = j + 1; k < friends[i].length(); k++) {
                        if (friends[i].charAt(k) == 'Y') {
                            ret[j] = ret[j].substring(0, k) + "Y" + ret[j].substring(k + 1, ret[j].length());
                            ret[k] = ret[k].substring(0,  j) + "Y" + ret[k].substring(j + 1, ret[k].length());
                        }
                    }
                }
            }
        }

        int max = 0;
        for (int i = 0; i < friends.length; i++) {
            int count = 0;
            for (int j = 0; j < friends[i].length(); j++) {
                if (ret[i].charAt(j) == 'Y') {
                    count++;
                }
            }
            max = Math.max(max, count);
        }
        return max;
    }

    public static void main(String[] args) {
        String[] friends = new String[]{"NYY", "YNY", "YYN"};
        int result = countFriends(friends);
        System.out.println(result);
    }
}