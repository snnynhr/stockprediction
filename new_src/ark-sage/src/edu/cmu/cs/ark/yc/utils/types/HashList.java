package edu.cmu.cs.ark.yc.utils.types;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

/**
 * A {@link Collection} (containing unique values) that can be accessed by its value or by index.
 * 
 * @author Yanchuan Sim
 * @version 0.1
 */
public class HashList<T> implements Collection<T>
{
  /**
   * {@link HashMap} whose key-value are element-index.
   */
  private final Map<T, Integer> M = new HashMap<>();

  /**
   * List of elements that we are storing.
   */
  private final List<T> L = new ArrayList<>();

  /**
   * An unmodifiable view of our {@link HashList}.
   */
  private final List<T> unmodifiable_view = Collections.unmodifiableList(L);

  /**
   * Returns the index of element <code>e</code>.
   * 
   * @param e
   *          Element to get index of.
   * @return the index of element <code>e</code>.
   */
  public Integer getIndex(T e)
  {
    return M.get(e);
  }

  /**
   * Returns the element at <code>index</code>.
   * 
   * @param index
   *          Position of element to get.
   * @return the element at <code>index</code>.
   */
  public T get(Integer index)
  {
    return L.get(index);
  }

  /*
   * (non-Javadoc)
   * @see java.util.Collection#add(java.lang.Object)
   */
  @Override
  public boolean add(T e)
  {
    if (M.containsKey(e))
      return false;

    M.put(e, L.size());
    return L.add(e);
  }

  /*
   * (non-Javadoc)
   * @see java.util.Collection#addAll(java.util.Collection)
   */
  @Override
  public boolean addAll(Collection<? extends T> c)
  {
    boolean ret = true;
    for (T e : c)
      ret &= add(e);

    return ret;
  }

  /*
   * (non-Javadoc)
   * @see java.util.Collection#clear()
   */
  @Override
  public void clear()
  {
    M.clear();
    L.clear();
  }

  /*
   * (non-Javadoc)
   * @see java.util.Collection#contains(java.lang.Object)
   */
  @Override
  public boolean contains(Object o)
  {
    return M.containsKey(o);
  }

  /*
   * (non-Javadoc)
   * @see java.util.Collection#containsAll(java.util.Collection)
   */
  @Override
  public boolean containsAll(Collection<?> c)
  {
    boolean ret = true;
    for (Object o : c)
      ret &= M.containsKey(o);
    return ret;
  }

  /*
   * (non-Javadoc)
   * @see java.util.Collection#isEmpty()
   */
  @Override
  public boolean isEmpty()
  {
    return L.isEmpty();
  }

  /*
   * (non-Javadoc)
   * @see java.util.Collection#iterator()
   */
  @Override
  public Iterator<T> iterator()
  {
    return L.iterator();
  }

  /*
   * (non-Javadoc)
   * @see java.util.Collection#remove(java.lang.Object)
   */
  @Override
  public boolean remove(Object o)
  {
    Integer i = M.get(o);
    if (i == null)
      return false;

    L.remove((int) i);
    for (int k = i; k < L.size(); k++)
      M.put(L.get(k), k - 1);

    return true;
  }

  /*
   * (non-Javadoc)
   * @see java.util.Collection#removeAll(java.util.Collection)
   */
  @Override
  public boolean removeAll(Collection<?> c)
  {
    boolean ret = true;
    for (Object o : c)
      ret &= remove(o);
    return ret;
  }

  /*
   * (non-Javadoc)
   * @see java.util.Collection#retainAll(java.util.Collection)
   */
  @SuppressWarnings("unchecked")
  @Override
  public boolean retainAll(Collection<?> c)
  {
    clear();
    addAll((Collection<T>) c);
    return true;
  }

  /*
   * (non-Javadoc)
   * @see java.util.Collection#size()
   */
  @Override
  public int size()
  {
    return L.size();
  }

  /*
   * (non-Javadoc)
   * @see java.util.Collection#toArray()
   */
  @Override
  public Object[] toArray()
  {
    return L.toArray();
  }

  /*
   * (non-Javadoc)
   * @see java.util.Collection#toArray(T[])
   */
  @SuppressWarnings("hiding")
  @Override
  public <T> T[] toArray(T[] a)
  {
    return L.toArray(a);
  }

  /*
   * (non-Javadoc)
   * @see java.lang.Object#toString()
   */
  @Override
  public String toString()
  {
    if (isEmpty())
      return "HashList [<empty>]";

    StringBuilder sb = new StringBuilder();
    sb.append("HashList[" + String.format("%d: %s", 0, get(0).toString()));
    for (int i = 1; i < size(); i++)
      sb.append(String.format(", %d: %s", i, get(i).toString()));

    return sb.append("]").toString();
  }

  /**
   * Returns an unmodifiable view of the list of items available. Items are ordered in the order that they are added.
   * 
   * @return an unmodifiable view of the list of items available.
   */
  public List<T> getUnmodifiableList()
  {
    return unmodifiable_view;
  }
}
