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
import Icon from "react-native-vector-icons/AntDesign";

const { width: SCREEN_WIDTH } = Dimensions.get("screen");

const RegistrationScreen = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [login, setLogin] = useState("");
  const [isSecure, setIsSecure] = useState(true);

  const showButton = (
    <TouchableOpacity
      onPress={() => setIsSecure((p) => !p)}
      style={styles.showButtonWrapper}
    >
      <Text style={styles.showButton}>Показати</Text>
    </TouchableOpacity>
  );

  const onSubmitHandler = () => {
    const values = { login, email, password };
    console.log(values);
    Keyboard.dismiss();
    setEmail("");
    setPassword("");
    setLogin("");
    setIsSecure(true);
  };

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
          <View style={styles.avatarWrapper}>
            <TouchableOpacity style={styles.addButton}>
              <Icon name="plus" size={16} style={styles.addButtonIcon} />
            </TouchableOpacity>
          </View>

          <Text style={styles.title}>Реєстрація</Text>

          <View style={[styles.innerContainer, styles.inputContainer]}>
            <Input
              placeholder="Логін"
              value={login}
              onChangeText={(login) => setLogin(login)}
            />

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
              <Text style={styles.loginButtonText}>Зареєстуватися</Text>
            </Button>

            <View style={styles.signUpContainer}>
              <Text style={styles.signUpText}>Вже є акаунт? </Text>
              <TouchableOpacity>
                <Text style={[styles.signUpText, styles.signUpRef]}>
                  Увійти
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
    position: "absolute",
    paddingHorizontal: 16,
    paddingTop: 92,
    bottom: 0,
    width: SCREEN_WIDTH,
    height: "70%",
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

export default RegistrationScreen;
