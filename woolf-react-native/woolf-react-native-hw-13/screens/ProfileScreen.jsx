import {
  View,
  Text,
  StyleSheet,
  Image,
  Dimensions,
  TouchableOpacity,
  FlatList,
} from "react-native";
import { colors } from "../styles/global";
import Icon from "react-native-vector-icons/AntDesign";
import avatarImage from "../assets/avatar.jpg";
import AddAvatarButton from "../components/AddAvatarButton";
import { posts } from "../utils/mockData";
import PostCard from "../components/PostCard";
import LogoutIcon from "../icons/LogoutIcon";

const { width: SCREEN_WIDTH } = Dimensions.get("screen");

const ProfileScreen = () => {
  return (
    <View style={styles.container}>
      <Image
        source={require("../assets/bgd.jpg")}
        style={styles.image}
        resizeMode="cover"
      />

      <View style={styles.innerContainer}>
        <AddAvatarButton isEmpty={false} />

        <View style={{ position: "absolute", right: 16, top: 22 }}>
          <LogoutIcon />
        </View>

        <Text
          style={{
            fontSize: 30,
            fontWeight: 500,
            textAlign: "center",
            marginBottom: 32,
          }}
        >
          Natali Romanova
        </Text>

        <FlatList
          data={posts}
          renderItem={({ item }) => <PostCard card={item} hasLikes />}
          keyExtractor={(item) => item.id}
          ItemSeparatorComponent={() => <View style={{ height: 32 }}></View>}
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, alignItems: "center", justifyContent: "center" },

  image: {
    position: "absolute",
    top: 0,
    bottom: 0,
    height: "100%",
    width: "100%",
  },

  innerContainer: {
    position: "absolute",
    paddingHorizontal: 16,
    paddingTop: 92,
    bottom: 0,
    width: SCREEN_WIDTH,
    height: "80%",
    backgroundColor: colors.white,
    borderTopLeftRadius: 25,
    borderTopRightRadius: 25,
    paddingBottom: 10,
  },

  avatarWrapper: {
    position: "absolute",
    top: -60,
    left: "50%",
    transform: [{ translateX: -50 }, { translateY: 0 }],
    width: 120,
    height: 120,
    backgroundColor: colors.light_gray,
    borderRadius: 16,
  },

  addButton: {
    position: "absolute",
    bottom: 14,
    right: 0,
    transform: [{ translateX: 12.5 }],
    width: 25,
    height: 25,

    alignItems: "center",
    justifyContent: "center",
    borderRadius: 100,
    backgroundColor: colors.white,
    borderColor: colors.orange,
    borderWidth: 1,
  },

  addButtonIcon: { color: colors.orange },
});

export default ProfileScreen;
