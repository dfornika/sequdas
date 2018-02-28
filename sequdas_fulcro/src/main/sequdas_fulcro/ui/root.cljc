(ns sequdas_fulcro.ui.root
  (:require
    [fulcro.client.mutations :as m]
    [fulcro.client.data-fetch :as df]
    translations.es                                         ; preload translations by requiring their namespace. See Makefile for extraction/generation
    [fulcro.client.dom :as dom]
    [sequdas_fulcro.api.mutations :as api]
    [fulcro.client.primitives :as prim :refer [defsc]]
    [fulcro.i18n :refer [tr trf]]))

;; The main UI of your application

(defsc Person [this {:keys [person/name person/age]}]
       { :initial-state (fn [{:keys [name age] :as params}] {:person/name name :person/age age}) }
       (dom/li nil
               (dom/h5 nil name (str "(age: " age ")"))))

(def ui-person (prim/factory Person {:keyfn :person/name}))

(defsc PersonList [this {:keys [person-list/label person-list/people]}]
       {:initial-state
        (fn [{:keys [label]}]
          {:person-list/label  label
           :person-list/people (if (= label "Friends")
                                 [(prim/get-initial-state Person {:name "Sally" :age 32})
                                  (prim/get-initial-state Person {:name "Joe" :age 22})]
                                 [(prim/get-initial-state Person {:name "Fred" :age 11})
                                  (prim/get-initial-state Person {:name "Bobby" :age 55})])})}
       (dom/div nil
                (dom/h4 nil label)
                (dom/ul nil
                        (map ui-person people))))

(def ui-person-list (prim/factory PersonList))

; Root's initial state becomes the entire app's initial state!
(defsc Root [this {:keys [ui/react-key friends enemies]}]
       {:initial-state (fn [params] {:friends (prim/get-initial-state PersonList {:label "Friends"})
                                     :enemies (prim/get-initial-state PersonList {:label "Enemies"})}) }
       (dom/div #js {:key react-key}
                (ui-person-list friends)
                (ui-person-list enemies)))