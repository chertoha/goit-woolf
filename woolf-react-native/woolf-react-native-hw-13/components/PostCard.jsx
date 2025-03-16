import { Image, StyleSheet, Text, TouchableOpacity, View } from "react-native";
import FeedbackIcon from "../icons/FeedbackIcon";
import LocationIcon from "../icons/LocationIcon";
import { useNavigation } from "@react-navigation/native";
import LikeIcon from "../icons/LikeIcon";

const PostCard = ({
  card: { img, title, comments, location, likes },
  hasLikes = false,
}) => {
  const navigation = useNavigation();
  return (
    <View style={styles.cardContainer}>
      <Image source={img} style={styles.cardImage} />

      <Text style={styles.cardTitle}>{title}</Text>

      <View style={styles.cardMeta}>
        <View style={{ flexDirection: "row", alignItems: "center", gap: 24 }}>
          <TouchableOpacity
            style={[styles.iconedWrapper, { gap: 6 }]}
            onPress={() => navigation.navigate("Comments")}
          >
            <Text>
              <FeedbackIcon />
            </Text>
            <Text>{comments}</Text>
          </TouchableOpacity>

          {hasLikes && (
            <View style={[styles.iconedWrapper, { gap: 6 }]}>
              <LikeIcon />
              <Text>{likes}</Text>
            </View>
          )}
        </View>

        <TouchableOpacity
          style={[styles.iconedWrapper, { gap: 3 }]}
          onPress={() => navigation.navigate("Map")}
        >
          <Text>
            <LocationIcon />
          </Text>
          <Text>{location}</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  cardContainer: {},

  cardImage: {
    borderRadius: 8,
    width: "100%",
    height: 240,
  },

  cardTitle: {
    marginTop: 8,
  },

  cardMeta: {
    marginTop: 8,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-between",
  },

  iconedWrapper: {
    display: "flex",
    flexDirection: "row",
    alignItems: "center",
  },

  cardComments: {},

  cardLocation: {},
});

export default PostCard;
