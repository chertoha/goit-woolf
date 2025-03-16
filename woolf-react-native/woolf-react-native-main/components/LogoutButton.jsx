import { TouchableOpacity } from "react-native";
import LogoutIcon from "../icons/LogoutIcon";
import { auth } from "../config";
import { useDispatch } from "react-redux";
import { logoutUser } from "../redux/auth/slice";
import { signOut } from "firebase/auth";

const LogoutButton = () => {
  const dispatch = useDispatch();

  const onLogout = () => {
    signOut(auth)
      .then(() => {
        // Sign-out successful.
        dispatch(logoutUser());
      })
      .catch((error) => {
        // An error happened.
        console.log("LogOut error", error);
      });
  };

  return (
    <TouchableOpacity onPress={onLogout}>
      <LogoutIcon />
    </TouchableOpacity>
  );
};
export default LogoutButton;
