(ns sequdas_fulcro.intro
  (:require [devcards.core :as rc :refer-macros [defcard]]
            [sequdas_fulcro.ui.components :as comp]))

(defcard SVGPlaceholder
  "# SVG Placeholder"
  (comp/ui-placeholder {:w 200 :h 200}))
