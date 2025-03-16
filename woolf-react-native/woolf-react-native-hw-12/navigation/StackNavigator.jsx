import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import LogoutIcon from "../icons/LogoutIcon";
import RegistrationScreen from "../screens/RegistrationScreen";
import LoginScreen from "../screens/LoginScreen";
import PostsScreen from "../screens/PostsScreen";
import BottomTabNavigator from "./BottomTabNavigator";
import CommentsScreen from "../screens/CommentsScreen";
import BackButton from "../components/BackButton";
import { StyleSheet } from "react-native";

const MainStack = createStackNavigator();

const StackNavigator = () => {
  const isLoggedIn = true;

  return (
    <NavigationContainer>
      <MainStack.Navigator
        initialRouteName="Login"
        screenOptions={{ headerShown: false }}
      >
        {isLoggedIn ? (
          <>
            <MainStack.Screen name="Home" component={BottomTabNavigator} />
            <MainStack.Screen
              name="Comments"
              component={CommentsScreen}
              options={{
                headerShown: true,
                title: "Коментарі",
                headerLeft: () => <BackButton />,
                headerStyle: {
                  borderBottomWidth: 1,
                  borderBottomColor: "#B3B3B3",
                },
                headerTitleAlign: "center",
                headerTitleStyle: styles.headerTitleStyle,
              }}
            />
          </>
        ) : (
          <>
            <MainStack.Screen
              name="Registration"
              component={RegistrationScreen}
            />
            <MainStack.Screen name="Login" component={LoginScreen} />
          </>
        )}
      </MainStack.Navigator>
    </NavigationContainer>
  );
};

const styles = StyleSheet.create({
  headerTitleStyle: {
    fontSize: 17,
    lineHeight: 22,
    paddingVertical: 11,
  },
});

export default StackNavigator;
