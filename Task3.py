class Playlist:
    def __init__(self,owner):
        self.owner = owner
        self.playlist = []

    def add_track(self,title,artist):
        self.playlist.append((title,artist))

    def remove_last(self):
        if self.playlist:
            deleted = self.playlist.pop()
            return deleted
        else:
            return None

    def total_track(self):
        return len(self.playlist)

    def unique_track(self):
        uniq = set(self.playlist)
        self.playlist = list(uniq)
        # for i in self.playlist:
        #     if self.playlist.count(i) > 1:
        #         self.playlist.remove(i)
        return self.playlist
    
    def search_by_title(self,title):
        return [i for i in self.playlist if title == i[0]]
    
    def filter_by_artist(self,artist):
        lst = []
        for i in self.playlist:
            if i[1] == artist:
                lst.append(i[0])
        return f"{artist}: {lst}"
    
a1 = Playlist("Aiden")
a1.add_track("Love the way you lie", "Eminem")
a1.add_track("Moon","Bruno Mars")
a1.add_track("Not Afraid","Eminem")
a1.add_track("Not Afraid","Eminem")
a1.add_track("Legacy","Eminem")
print(f"""
{a1.owner}:
Deleted: {a1.remove_last()}
Total: {a1.total_track()}
Unique playlist: {a1.unique_track()}
Searched: {a1.search_by_title("Moon")}
Artist: {a1.filter_by_artist("Eminem")}
""")