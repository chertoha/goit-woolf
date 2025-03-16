import {
  FlatList,
  Image,
  KeyboardAvoidingView,
  Platform,
  StyleSheet,
  Text,
  View,
} from "react-native";
import { colors } from "../styles/global";
import image from "../assets/not-woods.jpg";
import avatar_1 from "../assets/avatar.jpg";
import CommentCard from "../components/CommentCard";
import { TextInput } from "react-native-gesture-handler";
import ArrowBackIcon from "../icons/ArrowBackIcon";

const comments = [
  {
    id: 1,
    avatar: avatar_1,
    message:
      "Really love your most recent photo. I’ve been trying to capture the same thing for a few months and would love some tips!",
    datetime: "09 червня, 2020 | 08:40",
  },

  {
    id: 2,
    avatar: avatar_1,
    message:
      "A fast 50mm like f1.8 would help with the bokeh. I’ve been using primes as they tend to get a bit sharper images.",
    datetime: "09 червня, 2020 | 09:14",
  },

  {
    id: 3,
    avatar: avatar_1,
    message: "Thank you! That was very helpful!",
    datetime: "09 червня, 2020 | 09:20",
  },

  {
    id: 4,
    avatar: avatar_1,
    message:
      "A fast 50mm like f1.8 would help with the bokeh. I’ve been using primes as they tend to get a bit sharper images.",
    datetime: "09 червня, 2020 | 09:20",
  },
  {
    id: 5,
    avatar: avatar_1,
    message:
      "A fast 50mm like f1.8 would help with the bokeh. I’ve been using primes as they tend to get a bit sharper images.",
    datetime: "09 червня, 2020 | 09:20",
  },
];

const CommentsScreen = () => {
  return (
    <View style={styles.container}>
      <Image source={image} style={styles.image} />

      <FlatList
        data={comments}
        renderItem={({ item, index }) => (
          <CommentCard item={item} index={index} />
        )}
        keyExtractor={(item) => item.id}
        ItemSeparatorComponent={() => <View style={{ height: 24 }}></View>}
        style={{ marginTop: 32, paddingBottom: 16 }}
      />

      <KeyboardAvoidingView
        behavior={Platform.OS === "ios" ? "height" : "padding"}
      >
        <View
          style={{
            paddingTop: 32,
            position: "relative",
          }}
        >
          <TextInput
            placeholder="Коментувати..."
            style={styles.input}
            placeholderTextColor={colors.disabled_dark_gray}
          />

          <View style={styles.inputButton}>
            <ArrowBackIcon stroke={colors.white} />
          </View>
        </View>
      </KeyboardAvoidingView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.white,
    paddingTop: 32,
    paddingHorizontal: 16,
    paddingBottom: 16,
  },

  image: {
    width: "100%",
    height: 240,
    borderRadius: 8,
  },

  input: {
    paddingHorizontal: 16,
    backgroundColor: colors.light_gray,
    borderColor: colors.border_gray,
    borderWidth: 1,
    height: 50,
    borderRadius: 100,
  },

  inputButton: {
    width: 34,
    height: 34,
    borderRadius: 50,
    position: "absolute",
    backgroundColor: colors.orange,
    bottom: 8,
    right: 8,
    alignItems: "center",
    justifyContent: "center",
    transform: "rotate(90deg)",
  },
});

export default CommentsScreen;
