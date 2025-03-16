import {
  Dimensions,
  Image,
  Keyboard,
  KeyboardAvoidingView,
  Platform,
  StyleSheet,
  Text,
  TouchableOpacity,
  TouchableWithoutFeedback,
  View,
} from "react-native";
import { colors } from "../styles/global";
import Input from "../components/Input";
import { useState } from "react";
import Button from "../components/Button";
import { useNavigation } from "@react-navigation/native";

const { width: SCREEN_WIDTH } = Dimensions.get("screen");

const LoginScreen = () => {
  const navigation = useNavigation();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isSecure, setIsSecure] = useState(true);

  const onSubmitHandler = () => {
    const values = { email, password };
    console.log(values);
    Keyboard.dismiss();
    setEmail("");
    setPassword("");
    setIsSecure(true);
  };

  const showButton = (
    <TouchableOpacity
      onPress={() => setIsSecure((p) => !p)}
      style={styles.showButtonWrapper}
    >
      <Text style={styles.showButton}>Показати</Text>
    </TouchableOpacity>
  );

  return (
    <TouchableWithoutFeedback onPress={() => Keyboard.dismiss()}>
      <KeyboardAvoidingView
        style={styles.container}
        behavior={Platform.OS === "ios" ? "height" : "padding"}
      >
        <Image
          source={require("../assets/bgd.jpg")}
          style={styles.image}
          resizeMode="cover"
        />

        <View style={styles.formContainer}>
          <Text style={styles.title}>Увійти</Text>

          <View style={[styles.innerContainer, styles.inputContainer]}>
            <Input
              placeholder="Адреса електронної пошти"
              value={email}
              onChangeText={(email) => setEmail(email)}
            />

            <Input
              placeholder="Пароль"
              rightButton={showButton}
              outerStyles={styles.passwordButton}
              value={password}
              onChangeText={(password) => setPassword(password)}
              isSecure={isSecure}
            />
          </View>

          <View style={[styles.innerContainer, styles.buttonContainer]}>
            <Button onPress={onSubmitHandler}>
              <Text style={styles.loginButtonText}>Увійти</Text>
            </Button>

            <View style={styles.signUpContainer}>
              <Text style={styles.signUpText}>Немає акаунту? </Text>
              <TouchableOpacity
                onPress={() => navigation.navigate("Registration")}
              >
                <Text style={[styles.signUpText, styles.signUpRef]}>
                  Зареєструватися
                </Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </KeyboardAvoidingView>
    </TouchableWithoutFeedback>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, alignItems: "center", justifyContent: "center" },

  innerContainer: { gap: 16 },

  inputContainer: { marginTop: 32 },

  buttonContainer: { marginTop: 43 },

  image: {
    position: "absolute",
    top: 0,
    bottom: 0,
    height: "100%",
    width: "100%",
  },

  formContainer: {
    paddingHorizontal: 16,
    paddingTop: 32,
    position: "absolute",
    bottom: 0,
    width: SCREEN_WIDTH,
    height: "60%",
    backgroundColor: colors.white,
    borderTopLeftRadius: 25,
    borderTopRightRadius: 25,
  },

  title: {
    fontSize: 30,
    fontWeight: "500",
    lineHeight: 36,
    textAlign: "center",
  },

  showButtonWrapper: {
    position: "absolute",
    top: 0,
    right: 16,
    height: "100%",
    justifyContent: "center",
  },

  showButton: {
    fontSize: 16,
    lineHeight: 19,
    color: colors.blue,
  },

  passwordButton: {
    flexDirection: "row",
    justifyContent: "space-between",
  },

  loginButtonText: {
    color: colors.white,
    fontSize: 16,
    fontWeight: "400",
    lineHeight: 19,
    textAlign: "center",
  },

  signUpContainer: {
    marginTop: 16,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
  },

  signUpText: {
    color: colors.blue,
  },

  signUpRef: {
    textDecorationLine: "underline",
  },
});

export default LoginScreen;
