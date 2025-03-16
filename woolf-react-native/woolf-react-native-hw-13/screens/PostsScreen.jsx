import { FlatList, Image, StyleSheet, Text, View } from "react-native";
import { colors } from "../styles/global";
import avatarImage from "../assets/avatar.jpg";

import PostCard from "../components/PostCard";
import { posts } from "../utils/mockData";

const PostsScreen = () => {
  return (
    <View style={styles.container}>
      <View style={styles.userContainer}>
        <Image
          source={avatarImage}
          resizeMode="cover"
          style={styles.userAvatar}
        />
        <View>
          <Text style={styles.userName}>Natali Romanova</Text>
          <Text style={styles.userEmail}>email@example.com</Text>
        </View>
      </View>

      <View style={styles.list}>
        <FlatList
          data={posts}
          renderItem={({ item }) => <PostCard card={item} />}
          keyExtractor={(item) => item.id}
          ItemSeparatorComponent={() => <View style={{ height: 32 }}></View>}
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.white,
    paddingVertical: 32,
    paddingHorizontal: 16,
    paddingBottom: 80,
  },

  userContainer: {
    flexDirection: "row",
    alignItems: "center",
    gap: 8,
  },

  userAvatar: {
    borderRadius: 16,
    width: 60,
    height: 60,
  },

  userName: {
    fontSize: 13,
    fontWeight: "700",
  },

  userEmail: {
    fontSize: 11,
  },

  list: {
    marginTop: 32,
  },
});

export default PostsScreen;
