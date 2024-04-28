import { fetchImages } from '../pixabayAPI';
import { toast } from '../toast';

export function createGallery(
  render,
  {
    initialPage,
    initialQuery,
    initialList,
    limit,
    loader,
    smoothScroll,
    loadMore,
  }
) {
  let page = initialPage || 1;
  let query = initialQuery || '';
  let list = initialList || [];
  let total = null;

  async function fetchData() {
    if (!query) return;
    try {
      loader && loader.show();
      loadMore.hide();

      const data = await fetchImages(query, page, limit);

      // console.log('data', data);

      list.push(...data.list);
      total = data.total;

      const isEndCollection = limit * page >= total;
      const isCollectionEmpty = data.list.length === 0;

      if (isCollectionEmpty) {
        toast.emptyList();
      } else if (isEndCollection) {
        toast.endCollection();
      } else if (page === 1) {
        toast.foundTotal(total);
      }

      render(list);

      if (!isEndCollection) loadMore.show();

      smoothScroll && page !== 1 && !isCollectionEmpty && smoothScroll();
    } catch (error) {
      console.log('err', error);
      toast.fetchError();
    } finally {
      loader && loader.hide();
    }
  }

  return {
    getPage() {
      return page;
    },

    increasePage() {
      page += 1;
      fetchData();
    },

    resetPage() {
      page = 1;
    },

    setQuery(newQuery) {
      this.resetPage();
      this.clearList();
      query = newQuery;
      fetchData();
    },

    clearList() {
      list = [];
    },
  };
}
