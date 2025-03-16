import { StyleSheet, View } from "react-native";

import AddIcon from "react-native-vector-icons/AntDesign";
import { colors } from "../styles/global";

const AddButton = () => {
  return (
    <View style={styles.container}>
      <AddIcon name="plus" size={16} style={styles.icon} />
    </View>
  );
};

export default AddButton;

const styles = StyleSheet.create({
  container: {
    paddingHorizontal: 28,
    paddingVertical: 13,
    backgroundColor: colors.orange,
    borderRadius: 100,
  },

  icon: { color: "#FFFFFF" },
});
