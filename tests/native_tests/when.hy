(defn test-when []
  (assert (= (when True 1) 1))
  (assert (= (when True 1 2) 2))
  (assert (= (when True 1 3) 3))
  (assert (= (when False 2) None))
  (assert (= (when (= 1 2) 42) None))
  (assert (= (when (= 2 2) 42) 42))

  (assert (is (when (do (setv x 3) True)) None))
  (assert (= x 3)))
