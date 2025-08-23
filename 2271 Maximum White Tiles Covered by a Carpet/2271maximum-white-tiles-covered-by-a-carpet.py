class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        # Helper function to compute the number of tiles in a tile pack
        get_count = lambda t: t[1] - t[0] + 1

        # First, sort tiles by its start values
        tiles.sort(key = lambda x: x[0])

        # Left index of the sliding windows:
        # The index of the tile pack that is still under the carpet when the capret
        # is placed at the end of the tiles[r]
        l = 0

        # Number of tiles inside the current sliding window
        tiles_count = 0

        result = 0
        # The sliding window:
        # try to place the right end of the rug at the right end of every tile pack
        # and compute the max possible number of tiles under the rug
        for r in range(len(tiles)):
            tiles_count += get_count(tiles[r])

            # Move the left index till the moment when the end of the l-th tile is under the rug
            while tiles[r][1] - tiles[l][1] + 1 > carpetLen:
                tiles_count -= get_count(tiles[l])
                l += 1

            # The total length of the r-l tiles pack
            span = tiles[r][1] - tiles[l][0] + 1

            # The number of gaps in the pack = the total length of the pack - tiles count
            gaps = span - tiles_count

            # Update the result: it is equal to the min of rug/span - gaps
            # It works because all the tile gaps are under the rug
            result = max(result, min(span, carpetLen) - gaps)

        return result