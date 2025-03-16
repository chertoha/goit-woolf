import {
  Keyboard,
  KeyboardAvoidingView,
  Platform,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  TouchableWithoutFeedback,
  View,
} from "react-native";
import { colors } from "../styles/global";
import LocationIcon from "../icons/LocationIcon";
import Button from "../components/Button";
import CameraIcon from "../icons/CameraIcon";
import TrashIcon from "../icons/TrashIcon";

const CreatePostScreen = () => {
  return (
    <TouchableWithoutFeedback onPress={() => Keyboard.dismiss()}>
      <View style={styles.container}>
        <TouchableOpacity style={styles.image}>
          <View style={styles.imageInner}>
            <CameraIcon />
          </View>
        </TouchableOpacity>
        <Text style={[styles.text]}>Завантажте фото</Text>

        <KeyboardAvoidingView
          behavior={Platform.OS === "ios" ? "height" : "padding"}
        >
          <View style={[styles.input, { marginTop: 32 }]}>
            <TextInput
              placeholder="Назва..."
              placeholderTextColor={colors.disabled_dark_gray}
            />
          </View>

          <View style={[styles.input, { marginTop: 16 }]}>
            <Text>
              <LocationIcon />
            </Text>
            <TextInput
              placeholder="Місцевість..."
              placeholderTextColor={colors.disabled_dark_gray}
            />
          </View>
        </KeyboardAvoidingView>

        <View style={{ marginTop: 32 }}>
          <Button disabled>
            <Text style={[styles.buttonText, styles.text]}>Опубліковати</Text>
          </Button>
        </View>

        <TouchableOpacity
          style={{
            backgroundColor: colors.disabled_gray,
            width: 70,
            height: 40,
            alignItems: "center",
            justifyContent: "center",
            borderRadius: 100,
            marginTop: "auto",
            alignSelf: "center",
          }}
        >
          <TrashIcon />
        </TouchableOpacity>
      </View>
    </TouchableWithoutFeedback>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.white,
    paddingHorizontal: 16,
    paddingVertical: 32,
  },

  input: {
    height: 50,
    flexDirection: "row",
    alignItems: "center",
    gap: 4,
    borderBottomWidth: 1,
    borderColor: colors.border_gray,
  },

  buttonText: {
    textAlign: "center",
    fontSize: 16,
  },

  text: { color: colors.disabled_dark_gray },

  image: {
    marginBottom: 8,
    height: 240,
    backgroundColor: colors.disabled_gray,
    borderRadius: 8,
    alignItems: "center",
    justifyContent: "center",
    borderWidth: 1,
    borderColor: colors.border_gray,
  },

  imageInner: {
    width: 60,
    height: 60,
    backgroundColor: colors.white,
    borderRadius: 100,
    alignItems: "center",
    justifyContent: "center",
  },
});

export default CreatePostScreen;
