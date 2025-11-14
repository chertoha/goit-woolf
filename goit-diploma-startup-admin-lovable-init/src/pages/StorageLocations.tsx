import { useState } from "react";
import { Plus, Edit, Trash2, MapPin, Thermometer } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { mockStorageLocations, StorageLocation } from "@/data/mockData";
import { useToast } from "@/hooks/use-toast";

export default function StorageLocations() {
  const [locations, setLocations] =
    useState<StorageLocation[]>(mockStorageLocations);
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [editingLocation, setEditingLocation] =
    useState<StorageLocation | null>(null);
  const [formData, setFormData] = useState({
    name: "",
    description: "",
    temperature: "",
  });
  const { toast } = useToast();

  const resetForm = () => {
    setFormData({ name: "", description: "", temperature: "" });
    setEditingLocation(null);
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (editingLocation) {
      // Edit existing location
      setLocations((prev) =>
        prev.map((loc) =>
          loc.id === editingLocation.id ? { ...loc, ...formData } : loc
        )
      );
      toast({
        title: "Storage location updated",
        description: "The storage location has been successfully updated.",
      });
    } else {
      // Add new location
      const newLocation: StorageLocation = {
        id: Date.now().toString(),
        ...formData,
      };
      setLocations((prev) => [...prev, newLocation]);
      toast({
        title: "Storage location added",
        description: "The new storage location has been successfully created.",
      });
    }

    setIsDialogOpen(false);
    resetForm();
  };

  const handleEdit = (location: StorageLocation) => {
    setEditingLocation(location);
    setFormData({
      name: location.name,
      description: location.description,
      temperature: location.temperature || "",
    });
    setIsDialogOpen(true);
  };

  const handleDelete = (id: string) => {
    setLocations((prev) => prev.filter((loc) => loc.id !== id));
    toast({
      title: "Storage location deleted",
      description: "The storage location has been successfully removed.",
    });
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-foreground">
            Storage Locations
          </h1>
          <p className="text-muted-foreground">
            Manage your medicine storage areas
          </p>
        </div>

        <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
          <DialogTrigger asChild>
            <Button
              onClick={resetForm}
              className="bg-primary hover:bg-primary/90"
            >
              <Plus className="w-4 h-4 mr-2" />
              Add Location
            </Button>
          </DialogTrigger>

          <DialogContent>
            <DialogHeader>
              <DialogTitle>
                {editingLocation
                  ? "Edit Storage Location"
                  : "Add New Storage Location"}
              </DialogTitle>
            </DialogHeader>

            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <Label htmlFor="name">Name</Label>
                <Input
                  id="name"
                  value={formData.name}
                  onChange={(e) =>
                    setFormData((prev) => ({ ...prev, name: e.target.value }))
                  }
                  placeholder="e.g., Refrigerator Unit 1"
                  required
                />
              </div>

              <div>
                <Label htmlFor="description">Description</Label>
                <Textarea
                  id="description"
                  value={formData.description}
                  onChange={(e) =>
                    setFormData((prev) => ({
                      ...prev,
                      description: e.target.value,
                    }))
                  }
                  placeholder="Brief description of the storage location"
                  required
                />
              </div>

              <div>
                <Label htmlFor="temperature">Temperature (Optional)</Label>
                <Input
                  id="temperature"
                  value={formData.temperature}
                  onChange={(e) =>
                    setFormData((prev) => ({
                      ...prev,
                      temperature: e.target.value,
                    }))
                  }
                  placeholder="e.g., 2-8°C or Room temperature"
                />
              </div>

              <div className="flex gap-2 pt-4">
                <Button type="submit" className="flex-1">
                  {editingLocation ? "Update Location" : "Add Location"}
                </Button>
                <Button
                  type="button"
                  variant="outline"
                  onClick={() => {
                    setIsDialogOpen(false);
                    resetForm();
                  }}
                >
                  Cancel
                </Button>
              </div>
            </form>
          </DialogContent>
        </Dialog>
      </div>

      {/* Storage Locations Grid */}
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {locations.map((location) => (
          <Card key={location.id} className="hover:shadow-md transition-shadow">
            <CardHeader className="pb-3">
              <div className="flex items-start justify-between">
                <div className="flex items-center gap-2">
                  <div className="p-2 bg-primary/10 rounded-md">
                    <MapPin className="w-4 h-4 text-primary" />
                  </div>
                  <CardTitle className="text-lg">{location.name}</CardTitle>
                </div>

                <div className="flex gap-1">
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => handleEdit(location)}
                  >
                    <Edit className="w-4 h-4" />
                  </Button>
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => handleDelete(location.id)}
                    className="text-destructive hover:text-destructive"
                  >
                    <Trash2 className="w-4 h-4" />
                  </Button>
                </div>
              </div>
            </CardHeader>

            <CardContent className="space-y-3">
              <p className="text-sm text-muted-foreground">
                {location.description}
              </p>

              {location.temperature && (
                <div className="flex items-center gap-2 text-sm">
                  <Thermometer className="w-4 h-4 text-muted-foreground" />
                  <span className="text-muted-foreground">
                    {location.temperature}
                  </span>
                </div>
              )}
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
